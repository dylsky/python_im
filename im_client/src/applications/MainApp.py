import tkinter as tk

from src.controllers.MainAppController import MainAppController


def main():
    controller = MainAppController()
    # Build Gui and start it
    root = tk.Tk()
    root.title('Main Application')
    root.resizable(False, False)
    controller.init_view(root)
    print('Bye Bye')


if __name__ == "__main__":
    main()
