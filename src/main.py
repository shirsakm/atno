import tkinter as tk
import customtkinter as CTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Atno")
        self.root.geometry("650x350")
        self.root.resizable(False, False)


if __name__ == "__main__":
    root = CTk.CTk()
    app = App(root)
    root.mainloop()