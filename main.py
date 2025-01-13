from gui.main_window import FlyWizGui

def main():
    """
    The main function to run the Fly Wiz application.

    Initializes the FlyWizGui application and starts the main event loop.
    """
    try:
        app = FlyWizGui()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Entry point for the script.

    Calls the main function to start the Fly Wiz application.
    """
    main()