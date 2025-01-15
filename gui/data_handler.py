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
            'image': '',
            'flyer': '',
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
