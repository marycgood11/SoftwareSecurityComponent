#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from front_end import homepage

__author__ = "Mary Catherine Good"

"""
Welcome Page
- Will be able to sign into the application with your own name
"""
class WelcomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # welcome_frame
        # Create welcome_frame Widgets
        welcome_label = Label(self, text="Security Awareness Training", anchor="center", font=("Arial", 40), pady=10)
        home_button = Button(self, text="Go to home screen", command=lambda: controller.show_frame(homepage.HomePage), pady=5, width=20)

        # Layout welcome_frame Widgets
        # welcome_label.pack(anchor="center")
        welcome_label.grid(row=0, column=0)
        home_button.grid(row=1, column=0)
