#!/usr/bin/env python3
import tkinter as tk
from tkinter import *

__author__ = "Mary Catherine Good"

"""
Welcome Page
- Will be able to sign into the application with your own name
"""
class WelcomePage(tk.Frame):
    # TODO: IF TIME ENCRYPT USERNAME & CHECK AGAINST A DATABASE OF USERS
    # INITIALIZES THE WELCOME PAGE
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5BA3FF")

        # WELCOME PAGE WIDGETS
        sony_label = tk.Label(self, text="SONY", font=("Times", 55, "bold"), background="#5BA3FF")
        welcome_label = tk.Label(self, text="Security Awareness Training", font=("Noteworthy", 30), anchor="center", background="#5BA3FF", pady=15)
        self.username_entry = tk.Entry(self, foreground="#1A1A1A", width=25)
        place_holder_label = tk.Label(self, background="#5BA3FF")
        enter_button = tk.Button(self, text="Enter", font=(15), command=lambda: self.signin(parent, controller), pady=5, width=15)

        self.username_entry.insert(0, "Enter Name")

        # PLACE WIDETS ON FRAME
        sony_label.pack(side="top", fill="x", pady=40)
        welcome_label.pack()
        self.username_entry.pack()
        place_holder_label.pack()
        enter_button.pack()

    # GRABS USERNAME; IF A VALID NAME CONT. IF NOT THROW AN ERROR MSG
    def signin(self, parent, controller):
        self.username = self.username_entry.get()
        if self.username != "" and self.username != "Enter Name":
            controller.show_frame("HomePage")
        else:
            messagebox.showinfo("Username Error", "Please Enter Your Name")
