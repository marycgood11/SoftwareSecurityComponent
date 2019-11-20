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
