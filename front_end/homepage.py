#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from front_end import welcomepage

__author__ = "Mary Catherine Good"

"""
Home Page
- From here you will be able to navigate to play the game
"""
class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text="Home Page").pack()
        Button(self, text="Back to Welcome Page", command=lambda: controller.show_frame(welcomepage.WelcomePage)).pack()
