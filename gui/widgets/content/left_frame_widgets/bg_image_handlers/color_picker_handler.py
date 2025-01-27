from PIL import Image
from collections import Counter
import colorsys

class ColorPickerHandler:
    def __init__(self, data_handler, flyer_manipulator):
        self.data_handler = data_handler
        self.flyer_manipulator = flyer_manipulator

    def extract_colors(self):
        """
        Extract the two most represented colors and the darkest and lightest colors from the image(s).
        Store these colors in the data handler.
        """
        combined_image = self.data_handler.get_data().get('combined_image')
        image1 = self.data_handler.get_data().get('image1')
        image2 = self.data_handler.get_data().get('image2')

        if combined_image:
            self.extract_colors_from_image(combined_image)
        elif image1:
            self.extract_colors_from_image(image1)
        elif image2:
            self.extract_colors_from_image(image2)
        else:
            # No images provided, set default colors
            self.data_handler.update_data('bg_color', {
                'color1': (255, 255, 255),
                'color2': (255, 255, 255),
                'direction': 'Top to Bottom',
                'gradient_state': 1
            })
            self.data_handler.update_data('lightest_color', (255, 255, 255))
            self.data_handler.update_data('darkest_color', (0, 0, 0))

        # Print the extracted colors
        bg_color = self.data_handler.get_data().get('bg_color')
        lightest_color = self.data_handler.get_data().get('lightest_color')
        darkest_color = self.data_handler.get_data().get('darkest_color')
        print("Extracted colors:", bg_color, lightest_color, darkest_color)

        # Call the flyer manipulator to apply the background color
        self.flyer_manipulator.apply_background_color()
        print("Applied background color")

        # Update the flyer
        self.flyer_manipulator.main_app.update_flyer()

        # Update the GUI
        self.flyer_manipulator.main_app.update_gui()

    def extract_colors_from_image(self, image):
        """
        Extract the two most represented colors and the darkest and lightest colors from the image.
        Store these colors in the data handler.
        """
        lightest_and_darkest_colors, median_colors = self.analyze_image_colors(image)
        color1, color2 = median_colors
        lightest_color, darkest_color = lightest_and_darkest_colors

        self.data_handler.update_data('bg_color', {
            'color1': color1,
            'color2': color2,
            'direction': 'Top to Bottom',
            'gradient_state': 1
        })
        self.data_handler.update_data('lightest_color', lightest_color)
        self.data_handler.update_data('darkest_color', darkest_color)

    def filter_and_sort_colors(self, most_common_colors):
        """
        Filter out colors that are too similar and sort by lightness.
        """
        def color_distance(c1, c2):
            return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5
        
        filtered_colors = []
        for color, _ in most_common_colors:
            if all(color_distance(color, fc) > 30 for fc in filtered_colors):
                filtered_colors.append(color)
            if len(filtered_colors) >= 10:
                break
        
        hls_colors = []
        for color in filtered_colors:
            try:
                hls = colorsys.rgb_to_hls(*[c / 255.0 for c in color])
                hls_colors.append((hls, color))
            except ZeroDivisionError:
                continue
        
        hls_colors.sort(key=lambda x: x[0][1])
        sorted_colors = [color for hls, color in hls_colors]
        return sorted_colors

    def get_lightest_and_darkest_colors(self, sorted_colors):
        """
        Get the lightest and darkest colors from the sorted colors.
        """
        if len(sorted_colors) < 2:
            return [(255, 255, 255), (0, 0, 0)]
        
        lightest_color = sorted_colors[0]
        darkest_color = sorted_colors[-1]
        
        return [lightest_color, darkest_color]

    def get_median_colors(self, sorted_colors):
        """
        Get the median colors from the sorted colors.
        """
        middle_colors = sorted_colors[1:-1]
        
        median_index = len(middle_colors) // 2
        if len(middle_colors) % 2 == 0:
            median_colors = middle_colors[median_index - 5:median_index + 5]
        else:
            median_colors = middle_colors[median_index - 5:median_index + 5] if median_index > 4 else middle_colors[:10]
        
        unique_median_colors = []
        for color in median_colors:
            if color not in unique_median_colors:
                unique_median_colors.append(color)
            if len(unique_median_colors) >= 2:
                break
        
        while len(unique_median_colors) < 2:
            unique_median_colors.append((128, 128, 128))
        
        # Ensure color1 and color2 are distinct
        if len(unique_median_colors) >= 2 and self.color_distance(unique_median_colors[0], unique_median_colors[1]) < 30:
            for color in sorted_colors:
                if self.color_distance(unique_median_colors[0], color) >= 30:
                    unique_median_colors[1] = color
                    break
        
        return unique_median_colors

    def color_distance(self, c1, c2):
        """
        Calculate the Euclidean distance between two colors.
        """
        return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

    def analyze_image_colors(self, image):
        """
        Analyze the colors in the image and return the lightest, darkest, and median colors.
        """
        image = image.convert('RGB')
        
        max_resolution = 1080
        if max(image.size) > max_resolution:
            aspect_ratio = image.width / image.height
            if image.width > image.height:
                new_width = max_resolution
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = max_resolution
                new_width = int(new_height * aspect_ratio)
            image = image.resize((new_width, new_height), Image.LANCZOS)
        
        pixels = list(image.getdata())
        color_counts = Counter(pixels)
        most_common_colors = color_counts.most_common(50)
        most_common_colors = [(color, count) for color, count in most_common_colors if len(set(color)) > 1]
        
        sorted_colors = self.filter_and_sort_colors(most_common_colors)
        lightest_and_darkest_colors = self.get_lightest_and_darkest_colors(sorted_colors)
        median_colors = self.get_median_colors(sorted_colors)
        
        return lightest_and_darkest_colors, median_colors