from src.data_handler import DataHandler
from src.flyer_manipulator import FlyerManipulator
from gui.main_window import FlyWizGui

class FlyWizApp:
    def __init__(self):
        """
        Initializes the FlyWizApp class.
        """
        self.data_handler = DataHandler()
        self.flyer_manipulator = FlyerManipulator(self.data_handler, self)
        self.app = FlyWizGui(self.data_handler, self.flyer_manipulator)
        self.flyer_manipulator.main_app = self.app  

    def run(self):
        """
        Runs the FlyWizGui application.
        """
        try:
            self.app.mainloop()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Entry point for the script.

    Creates an instance of FlyWizApp and runs the application.
    """
    fly_wiz_app = FlyWizApp()
    fly_wiz_app.run()