#!/usr/bin/env python3
import tkinter as tk
from tkinter import *

__author__ = "Mary Catherine Good"

class Score(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5BA3FF")

        # ADD IN SCORE LABEL
        # ADD IN INFO TO IMPROVE PERSONAL SECURITY
        # ADD COMPLETE BUTTON - SENDS EMAIL TO ADMIN ACCOUNT

        self.score=0
