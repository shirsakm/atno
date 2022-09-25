import tkinter as tk
import customtkinter as CTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Atno")
        self.root.geometry("650x350")
        self.root.resizable(False, False)

        self.learn_tab = CTk.CTkFrame(self.root)
        self.learn_tab.place(x=0, y=0, width=575, height=350)

        CTk.CTkLabel(self.learn_tab, text="Elements", text_font=("Arial", 18)).place(x=10, y=20, width=120, height=25)

        self.element_list = tk.Listbox(self.learn_tab, background="#525252", borderwidth=0, highlightthickness=0)
        self.element_list.place(x=10, y=50, width=120, height=280)


if __name__ == "__main__":
    root = CTk.CTk()
    app = App(root)
    root.mainloop()