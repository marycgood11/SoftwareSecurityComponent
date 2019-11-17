#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from front_end import homepage
from front_end import welcomepage

__author__ = "Mary Catherine Good"

"""
Sets up navigation between the different frames of the application
"""
class UI_Setup(Tk):
    # INITIALIZES THE BASE FRAME AND THE LIST OF FRAMES IN THE APPLICATION
    def __init__(self, master):
        # INITILIZES THE BASE FRAME
        self.master = master
        self.master.title("TEST")
        self.master.geometry("700x400")

        tk.Frame.__init__(self, master)

        # WILL HOLD ALL FRAMES AS THEY ARE PLACED ON TOP OR TAKEN AWAY DURING NAVIGATION
        container = Frame(self.master)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        # KEEPS TRACK OF ALL FRAMES THAT CAN BE NAVIGATED TO
        # ADD NEW FRAMES TO THIS LIST
        for F in (welcomepage.WelcomePage, homepage.HomePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(welcomepage.WelcomePage)

    # NAVIGATES TO A NEW FRAME
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
