#!/usr/bin/env python3
import tkinter as tk
from tkinter import *

__author__ = "Mary Catherine Good"

"""
Home Page
- From here you will be able to navigate to play the game
"""
class HomePage(tk.Frame):
    # INITIALIZES THE HOMEPAGE
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E6F1FF")

        training_info = "This game is intended to test your knowledge of security.  It will test to see if you are an asset or a liability. \nThroughout the game, you will be presented with a set of scenarios.  It is up to you to choose the best option.  At the end you will receive a security score and any tips on how to improve your security habits.  These will not only help you become more secure in your online life, but also help protect you and SONY Corporation from being hacked. \nTo begin playing, click the button below. \nGood Luck.  May the most security savy person win!"

        # CREATE FRAMES
        title_frame = tk.Frame(self, background="#E6F1FF", width=550, pady=10)
        border_frame1 = tk.Frame(self, background="#5BA3FF", height=2, width=550)
        border_frame2 = tk.Frame(self, background="#006EFF", height=2, width=550)
        border_frame3 = tk.Frame(self, background="white", height=2, width=550)
        border_frame4 = tk.Frame(self, background="#006EFF", height=2, width=550)
        border_frame5 = tk.Frame(self, background="#5BA3FF", height=2, width=550)
        main_frame = tk.Frame(self, background="#E6F1FF", height=900, width=550)

        # LAYOUT FRAMES
        title_frame.grid(row=0, column=0, sticky="nsew")
        border_frame1.grid(row=1, column=0, sticky="new")
        border_frame2.grid(row=2, column=0, sticky="new")
        border_frame3.grid(row=3, column=0, sticky="new")
        border_frame4.grid(row=4, column=0, sticky="new")
        border_frame5.grid(row=5, column=0, sticky="new")
        main_frame.grid(row=6, column=0)

        # HOME PAGE WIDGETS
        security_awareness_label = tk.Label(title_frame, text="Security Awareness Training", font=("Noteworthy", 30), anchor="center", background="#E6F1FF", pady=15)
        information_label = tk.Label(main_frame, text=training_info, wraplength=425, justify="left", background="#E6F1FF", pady=20)
        place_holder_label = tk.Label(main_frame, background="#E6F1FF")
        start_button = tk.Button(main_frame, text="Let's Begin!", font=(15), command=lambda: controller.show_frame("Scenario1"), highlightbackground="#5BA3FF", pady=5, width=15)

        # PLACE WIDGETS ON FRAME
        security_awareness_label.pack()
        information_label.pack()
        place_holder_label.pack()
        start_button.pack()
