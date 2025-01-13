from gui.main_window import FlyWizGui

def main():
    try:
        app = FlyWizGui()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()