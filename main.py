from data_handler import DataHandler
from flyer_manipulator import FlyerManipulator
from gui.main_window import FlyWizGui

def main():
    """
    The main function to run the Fly Wiz application.

    Initializes the FlyWizGui application and starts the main event loop.
    """
    try:
        data_handler = DataHandler()
        flyer_manipulator = FlyerManipulator(data_handler)
        app = FlyWizGui(data_handler, flyer_manipulator)
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Entry point for the script.

    Calls the main function to start the Fly Wiz application.
    """
    main()