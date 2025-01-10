from PIL import Image, ImageDraw, ImageFilter
from collections import Counter
import colorsys

def color_picker(image_path):
    def filter_and_sort_colors(most_common_colors):
        # Function to calculate the Euclidean distance between two colors
        def color_distance(c1, c2):
            return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5
        
        # Filter out colors that are too similar
        filtered_colors = []
        for color, _ in most_common_colors:
            if all(color_distance(color, fc) > 30 for fc in filtered_colors):  # Adjust the threshold to allow more colors
                filtered_colors.append(color)
            if len(filtered_colors) >= 10:
                break
        
        # Convert filtered colors to HLS and sort by lightness
        hls_colors = []
        for color in filtered_colors:
            try:
                hls = colorsys.rgb_to_hls(*[c / 255.0 for c in color])  # Normalize RGB values to 0-1
                hls_colors.append((hls, color))
            except ZeroDivisionError:
                continue  # Skip colors that cause division by zero
        
        hls_colors.sort(key=lambda x: x[0][1])  # Sort by lightness
        
        # Extract the sorted colors
        sorted_colors = [color for hls, color in hls_colors]
        return sorted_colors

    def get_lightest_and_darkest_colors(sorted_colors): 
        # Check if we have enough colors to proceed
        if len(sorted_colors) < 2:
            # Fallback to default colors if not enough colors are available
            return [(255, 255, 255), (0, 0, 0)]
        
        # Identify the lightest and darkest colors
        lightest_color = sorted_colors[0]
        darkest_color = sorted_colors[-1]
        
        return [lightest_color, darkest_color]

    def get_median_colors(sorted_colors):
        # Exclude the first and last colors
        middle_colors = sorted_colors[1:-1]
        
        # Calculate the median colors
        median_index = len(middle_colors) // 2
        if len(middle_colors) % 2 == 0:
            median_colors = middle_colors[median_index - 5:median_index + 5]
        else:
            median_colors = middle_colors[median_index - 5:median_index + 5] if median_index > 4 else middle_colors[:10]
        
        # Ensure we always have 2 different median colors
        unique_median_colors = []
        for color in median_colors:
            if color not in unique_median_colors:
                unique_median_colors.append(color)
            if len(unique_median_colors) >= 2:
                break
        
        # Add fallback colors if needed
        while len(unique_median_colors) < 2:
            unique_median_colors.append((128, 128, 128))
        
        return unique_median_colors

    image = Image.open(image_path)
    image = image.convert('RGB')
    
    # Resize the image if its resolution is above 1080p
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
    
    # Count the frequency of each color
    color_counts = Counter(pixels)
    
    # Get the 50 most common colors to ensure we have enough to choose from
    most_common_colors = color_counts.most_common(50)
    
    # Filter out grayscale colors (where R, G, and B are the same)
    most_common_colors = [(color, count) for color, count in most_common_colors if len(set(color)) > 1]
    
    # Get the filtered and sorted colors
    sorted_colors = filter_and_sort_colors(most_common_colors)
    
    # Get the lightest and darkest colors
    lightest_and_darkest_colors = get_lightest_and_darkest_colors(sorted_colors)
    
    # Get the median colors
    median_colors = get_median_colors(sorted_colors)
    
    return lightest_and_darkest_colors, median_colors

def apply_background_color(flyer_image, color_list):
    width, height = flyer_image.size
    gradient = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(gradient)

    for y in range(height):
        ratio = y / height
        r = int(color_list[0][0] * (1 - ratio) + color_list[1][0] * ratio)
        g = int(color_list[0][1] * (1 - ratio) + color_list[1][1] * ratio)
        b = int(color_list[0][2] * (1 - ratio) + color_list[1][2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    flyer_image = Image.alpha_composite(flyer_image.convert('RGBA'), gradient.convert('RGBA'))
    return flyer_image

def background_text_color(flyer_image, current_data):
    image_path = current_data["file_path"]
    lightest_and_darkest_colors, median_colors = color_picker(image_path)

    flyer_image = apply_background_color(flyer_image, median_colors)

    return flyer_image, lightest_and_darkest_colors