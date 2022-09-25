from mimetypes import common_types
import tkinter as tk
import customtkinter as CTk
import json
import random
from tkinter.messagebox import showinfo

CTk.set_default_color_theme("dark-blue")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Atno")
        self.root.geometry("650x350")
        self.root.resizable(False, False)

        self.elements = json.load(open("data.json", "r", encoding="utf-8"))["elements"]
        
        self.learn_tab = CTk.CTkFrame(self.root)

        L = tk.PhotoImage(file="assets/L.png")
        AN = tk.PhotoImage(file="assets/AN.png")
        MN = tk.PhotoImage(file="assets/MN.png")

        self.root.L = L
        self.root.AN = AN
        self.root.MN = MN

        self.learn_btn = tk.Button(self.root, text="Learn", command=self.open_learn, image=L, borderwidth=0, highlightthickness=0)
        self.learn_btn.place(x=595, y=90, width=45, height=45)

        self.atom_practice_btn = tk.Button(self.root, text="Quiz 1", command=self.open_atom_practice, image=AN, borderwidth=0, highlightthickness=0)
        self.atom_practice_btn.place(x=595, y=140, width=45, height=45)
        self.current_atom_element = random.randint(0, len(self.elements) - 1)

        self.mass_practice_btn = tk.Button(self.root, text="Quiz 2", command=self.open_mass_practice, image=MN, borderwidth=0, highlightthickness=0)
        self.mass_practice_btn.place(x=595, y=190, width=45, height=45)
        self.current_mass_element = random.randint(0, len(self.elements) - 1)

        CTk.CTkLabel(self.learn_tab, text="Elements", text_font=("Arial", 18)).place(x=10, y=20, width=120, height=25)

        self.element_list = tk.Listbox(self.learn_tab, background="#525252", borderwidth=0, highlightthickness=0, font=("Arial", 10), foreground="#ffffff")
        self.element_list.place(x=10, y=50, width=120, height=280)
        scroll = tk.Scrollbar(self.learn_tab, orient="vertical", command=self.element_list.yview)
        scroll.place(x=130, y=50, width=15, height=280)
        self.element_list.config(yscrollcommand=scroll.set)

        for e in self.elements:
            self.element_list.insert(tk.END, f"{e['number']} {e['name']}")

        self.element_list.bind("<<ListboxSelect>>", self.select_element)
        
        self.element_name = CTk.CTkLabel(self.learn_tab, text="Element Name", text_font=("Arial", 18))
        self.element_name.place(x=150, y=20, width=425, height=60)

        self.data_frame = CTk.CTkFrame(self.learn_tab)
        self.data_frame.place(x=170, y=90, width=380, height=215)

        CTk.CTkLabel(self.data_frame, text="Symbol", text_font=("Arial", 12)).place(x=20, y=10, width=145, height=25)
        CTk.CTkLabel(self.data_frame, text="Electronic Config", text_font=("Arial", 12)).place(x=20, y=50, width=145, height=25)
        CTk.CTkLabel(self.data_frame, text="Atomic Number", text_font=("Arial", 12)).place(x=20, y=90, width=145, height=25)
        CTk.CTkLabel(self.data_frame, text="Mass Number", text_font=("Arial", 12)).place(x=20, y=130, width=145, height=25)
        CTk.CTkLabel(self.data_frame, text="Period, Group Number", text_font=("Arial", 12)).place(x=20, y=170, width=145, height=25)

        self.symbol = CTk.CTkLabel(self.data_frame, text="", text_font=("Arial", 12))
        self.symbol.place(x=175, y=10, width=195, height=25)
        self.elec_conf = CTk.CTkLabel(self.data_frame, text="", text_font=("Arial", 12))
        self.elec_conf.place(x=175, y=50, width=195, height=25)
        self.at_no = CTk.CTkLabel(self.data_frame, text="", text_font=("Arial", 12))
        self.at_no.place(x=175, y=90, width=195, height=25)
        self.ma_no = CTk.CTkLabel(self.data_frame, text="", text_font=("Arial", 12))
        self.ma_no.place(x=175, y=130, width=195, height=25)
        self.pg_no = CTk.CTkLabel(self.data_frame, text="", text_font=("Arial", 12))
        self.pg_no.place(x=175, y=170, width=195, height=25)

        self.select_element(None, 0)

        self.atom_practice_tab = CTk.CTkFrame(self.root)
        CTk.CTkLabel(self.atom_practice_tab, text="Guess Atomic Number", text_font=("Arial", 28)).place(x=10, y=20, width=560, height=50)
        self.current_atom_element_label = CTk.CTkLabel(self.atom_practice_tab, text=self.elements[self.current_atom_element]["name"], text_font=("Arial", 28))
        self.current_atom_element_label.place(x=150, y=95, width=280, height=50)

        self.current_atom_answer_input = tk.Entry(self.atom_practice_tab, font=("Arial", 22), background="#525252", foreground="#ffffff", borderwidth=0, highlightthickness=0)
        self.current_atom_answer_input.place(x=150, y=150, width=280, height=50)

        self.current_atom_answer_input.bind("<Return>", self.check_atom_answer)

        self.current_atom_answer_submit_btn = CTk.CTkButton(self.atom_practice_tab, text="Submit", command=self.check_atom_answer)
        self.current_atom_answer_submit_btn.place(x=150, y=210, width=280, height=50)

        self.mass_practice_tab = CTk.CTkFrame(self.root)
        CTk.CTkLabel(self.mass_practice_tab, text="Guess Mass Number", text_font=("Arial", 28)).place(x=10, y=20, width=560, height=50)
        self.current_mass_element_label = CTk.CTkLabel(self.mass_practice_tab, text=self.elements[self.current_mass_element]["name"], text_font=("Arial", 28))
        self.current_mass_element_label.place(x=150, y=95, width=280, height=50)

        self.current_mass_answer_input = tk.Entry(self.mass_practice_tab, font=("Arial", 22), background="#525252", foreground="#ffffff", borderwidth=0, highlightthickness=0)
        self.current_mass_answer_input.place(x=150, y=150, width=280, height=50)

        self.current_mass_answer_input.bind("<Return>", self.check_mass_answer)

        self.current_mass_answer_submit_btn = CTk.CTkButton(self.mass_practice_tab, text="Submit", command=self.check_mass_answer)
        self.current_mass_answer_submit_btn.place(x=150, y=210, width=280, height=50)

        self.open_learn()


    def check_atom_answer(self, event=None):
        if self.elements[self.current_atom_element]["number"] == int(self.current_atom_answer_input.get()):
            self.current_atom_answer_input.delete(0, tk.END)
            showinfo("Correct", "Correct!")
            self.current_atom_element = random.randint(0, len(self.elements) - 1)
            self.current_atom_element_label.config(text=self.elements[self.current_atom_element]["name"])
        else:
            self.current_atom_answer_input.delete(0, tk.END)
            showinfo("Incorrect", f"Incorrect!, Correct answer is {self.elements[self.current_atom_element]['number']}")

    def check_mass_answer(self, event=None):
        mass = self.elements[self.current_mass_element]['atomic_mass']
        if int(self.elements[self.current_mass_element]["atomic_mass"]) == int(self.current_mass_answer_input.get()):
            self.current_mass_answer_input.delete(0, tk.END)
            showinfo("Correct", f"Correct! ({mass})")
            self.current_mass_element = random.randint(0, len(self.elements) - 1)
            self.current_mass_element_label.config(text=self.elements[self.current_mass_element]["name"])
        else:
            self.current_mass_answer_input.delete(0, tk.END)
            showinfo("Incorrect", f"Incorrect!, Correct answer is {int(mass)} ({mass})")

    def select_element(self, event, index=None):
        index = self.element_list.curselection()[0] if index is None else index
        element = self.elements[index]
        self.element_name.config(text=element["name"])
        self.symbol.config(text=element["symbol"])
        self.elec_conf.config(text=element["electron_configuration_semantic"])
        self.at_no.config(text=str(element["number"]))
        self.ma_no.config(text=str(element["atomic_mass"]))
        self.pg_no.config(text=f"{element['xpos']}, {element['ypos']}")

    def open_learn(self):
        self.learn_tab.place(x=0, y=0, width=575, height=350)
        self.atom_practice_tab.place_forget()
        self.mass_practice_tab.place_forget()

    def open_atom_practice(self):
        self.learn_tab.place_forget()
        self.atom_practice_tab.place(x=0, y=0, width=575, height=350)
        self.mass_practice_tab.place_forget()

    def open_mass_practice(self):
        self.learn_tab.place_forget()
        self.atom_practice_tab.place_forget()
        self.mass_practice_tab.place(x=0, y=0, width=575, height=350)

    def load_ass(self):
        self.at_no_icon = tk.PhotoImage(file="assets/AN.png")
        self.learn_icon = tk.PhotoImage(file="assets/L.png").subsample(3, 3)
        self.mass_no_icon = tk.PhotoImage(file="assets/MN.png")
        self.elements = json.load(open("data.json", "r", encoding="utf-8"))["elements"]

if __name__ == "__main__":
    root = CTk.CTk()
    app = App(root)
    root.mainloop()