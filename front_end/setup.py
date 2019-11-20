#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from front_end import homepage
from front_end import welcomepage
from front_end import scenarios

__author__ = "Mary Catherine Good"

"""
Sets up navigation between the different frames of the application
"""
class UI_Setup(tk.Tk):
    # SETS UP THE UI
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # WINDOW PROPERTIES
        self.title("SONY Corporation")
        self.geometry("550x650")

        # CONTAINER FOR THE FRAMES INITIALIZATION
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # ALL THE FRAMES IN THE APPLICATION
        self.frames = {}
        for F in (welcomepage.WelcomePage, homepage.HomePage, scenarios.Scenario1, scenarios.Scenario2, scenarios.Scenario3):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    # NAVIGATE TO THE DIFFERENT FRAMES IN THE APPLICATION
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



"""class UI_Setup(Tk):
    # INITIALIZES THE BASE FRAME AND THE LIST OF FRAMES IN THE APPLICATION
    def __init__(self, master):
        # INITILIZES THE BASE FRAME
        self.master = master
        self.master.title("SONY Security Awareness Training")
        self.master.geometry("550x650")
        # Layout Frame Containers
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        Frame.__init__(self, master)

        # WILL HOLD ALL FRAMES AS THEY ARE PLACED ON TOP OR TAKEN AWAY DURING NAVIGATION
        container = Frame(self.master, bg="#4A87FF")
        container.pack(fill="both", expand=True)

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
"""
