# FILE: gui/data_handler.py

class DataHandler:
    """
    A class to handle data from the GUI.

    Attributes
    ----------
    data : dict
        A dictionary to store the data from the GUI.

    Methods
    -------
    update_data(key, value):
        Updates the data dictionary with the given key-value pair.
    get_data():
        Returns the data dictionary.
    """
    def __init__(self):
        """
        Initializes the DataHandler with an empty data dictionary.
        """
        self.data = {}

    def update_data(self, key, value):
        """
        Updates the data dictionary with the given key-value pair.

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