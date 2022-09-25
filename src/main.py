import tkinter as tk
import customtkinter as CTk
import json

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Atno")
        self.root.geometry("650x350")
        self.root.resizable(False, False)

        self.elemets = json.load(open("data.json", "r", encoding="utf-8"))["elements"]

        self.learn_tab = CTk.CTkFrame(self.root)
        self.learn_tab.place(x=0, y=0, width=575, height=350)

        CTk.CTkLabel(self.learn_tab, text="Elements", text_font=("Arial", 18)).place(x=10, y=20, width=120, height=25)

        self.element_list = tk.Listbox(self.learn_tab, background="#525252", borderwidth=0, highlightthickness=0, font=("Arial", 10), foreground="#ffffff")
        self.element_list.place(x=10, y=50, width=120, height=280)
        scroll = tk.Scrollbar(self.learn_tab, orient="vertical", command=self.element_list.yview)
        scroll.place(x=130, y=50, width=15, height=280)
        self.element_list.config(yscrollcommand=scroll.set)

        for e in self.elemets:
            self.element_list.insert(tk.END, f"{e['number']} {e['name']}")

        self.element_list.bind("<<ListboxSelect>>", self.select_element)
        
        self.element_name = CTk.CTkLabel(self.learn_tab, text="Element Name", text_font=("Arial", 18))
        self.element_name.place(x=150, y=20, width=425, height=60)


    def select_element(self, event):
        index = self.element_list.curselection()[0]
        element = self.elemets[index]
        print(element["name"])
        self.element_name.config(text=element["name"])

if __name__ == "__main__":
    root = CTk.CTk()
    app = App(root)
    root.mainloop()