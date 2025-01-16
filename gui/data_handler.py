import base64
import json
from io import BytesIO
from PIL import Image

class DataHandler:
    """
    A class to handle data from the GUI and notify observers of changes.

    Attributes
    ----------
    data : dict
        A dictionary to store the data from the GUI.
    observers : list
        A list of observer functions to notify when data changes.

    Methods
    -------
    update_data(key, value):
        Updates the data dictionary with the given key-value pair and notifies observers.
    get_data():
        Returns the data dictionary.
    add_observer(observer):
        Adds an observer function to the list of observers.
    remove_observer(observer):
        Removes an observer function from the list of observers.
    notify_observers(key, value):
        Notifies all observer functions of data changes.
    image_to_base64(image):
        Converts a Pillow image to a base64 string.
    base64_to_image(base64_str):
        Converts a base64 string to a Pillow image.
    save(file_path):
        Saves the data dictionary as a JSON file, converting images to base64 if necessary.
    """
    def __init__(self):
        """
        Initializes the DataHandler with an empty data dictionary and an empty list of observers.
        """
        self.data = {
            'title': '',
            'styled_info': '',
            'text_info': '',
            'footer': '',
            'image1': None,
            'image2': None,
            'flyer': None
        }

    def update_data(self, key, value):
        """
        Updates the data dictionary with the given key-value pair and notifies observers.

        Parameters
        ----------
        key : str
            The key for the data.
        value : any
            The value for the data.
        """
        self.data[key] = value

    def get_data(self):
        """
        Returns the data dictionary.

        Returns
        -------
        dict
            The data dictionary.
        """
        return self.data

    def image_to_base64(self, image):
        """
        Converts a Pillow image to a base64 string.

        Parameters
        ----------
        image : Image
            The Pillow image to convert.

        Returns
        -------
        str
            The base64 string representation of the image.
        """
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str

    def base64_to_image(self, base64_str):
        """
        Converts a base64 string to a Pillow image.

        Parameters
        ----------
        base64_str : str
            The base64 string to convert.

        Returns
        -------
        Image
            The Pillow image.
        """
        img_data = base64.b64decode(base64_str)
        image = Image.open(BytesIO(img_data))
        return image

    def save(self, file_path):
        """
        Saves the data dictionary as a JSON file, converting images to base64 if necessary.

        Parameters
        ----------
        file_path : str
            The file path to save the JSON file.
        """
        data_to_save = self.data.copy()

        # Convert images to base64 if they are not None
        for key in ['image1', 'image2', 'flyer']:
            if isinstance(data_to_save[key], Image.Image):
                data_to_save[key] = self.image_to_base64(data_to_save[key])

        with open(file_path, 'w') as json_file:
            json.dump(data_to_save, json_file, indent=4)