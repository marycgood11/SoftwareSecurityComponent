#!/usr/bin/env python3
import subprocess
import tkinter as tk

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import main

__author__ = "Mary Catherine Good"

# UPLOAD SCHEDULE WINDOW
class Home:
    # INITIALIZE HOME SCREEN WINDOW AND CREATE BASE FRAMES
    def __init__(self, master):
        self.file_name = ""
        # Set up Window
        self.master = master
        self.master.title("Security Awareness Training")
        self.master.geometry("700x400")

        # Create Frame Containers
        main_frame = Frame(self.master, bg='#eee6ff', width=800, highlightbackground="lavender", highlightcolor="lavender", highlightthickness=1,)

        # Layout Frame Containers
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        main_frame.grid(row=0, column=1, sticky="nsew")

        # Set up main_frame
        self.main_f(main_frame)

    # CREATES MAIN FRAME WIDGETS AND PLACES THEM ON THE GRID
    # ADDS FUNCTIONALITY TO WIDGETS
    def main_f(self, main_frame):
        # Create Frames w/in main_frame
        title_frame = Frame(main_frame, background="#f1eff5", height=100, width=1000, pady=10)
        border_frame = Frame(main_frame, background="#484848", height=2, width=1000)
        upload_frame = Frame(main_frame, bg='#eee6ff', height=900, width=1000)

        # Layout Frames w/in main_frame
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        title_frame.grid(row=0, column=0, sticky="nsew")
        border_frame.grid(row=1, column=0, sticky="new")
        upload_frame.grid(row=1, column=0)

        # title_frame
        # Create title_frame Widgets
        title_label = tk.Label(title_frame, text="Security Awareness Training", anchor="center", background="#f1eff5", font=("Arial", 40), foreground="#484848", pady=10)
        # Layout title_frame Widgets
        title_label.pack(anchor="center")

        # upload_frame
        # Create upload_frame Widgets
        upload_button = tk.Button(upload_frame, text="Test Button1", command=lambda: self.upload_requirements(filename_label), pady=5, width=20)
        generate_schedule_button = tk.Button(upload_frame, text="Test Button2", command=lambda: self.generate_schedule(), pady=5, width=20)

        upload_reqs_title_label = tk.Label(upload_frame, text="Help Button (?)", background="#eee6ff", font=("Arial", 25), foreground="#484848", pady=15)
        filename_label = tk.Label(upload_frame, text="File Name", background="#eee6ff", state="disabled", pady=5)

        # Binds click event to label - if clicked a message pops up giving help instructions
        upload_reqs_title_label.bind("<Button-1>", self.upload_help)

        # Layout upload_frame Widgets
        upload_reqs_title_label.grid(row=0, column=0)
        upload_button.grid(row=1, column=0)
        filename_label.grid(row=2, column=0)
        generate_schedule_button.grid(row=3, column=0)

    # DISPLAYS A HELP MESSAGE THAT EXPLAINS HOW THE INPUT SHOULD BE FORMATTED
    def upload_help(self, event):
        print("Upload Requirements MessageBox")
        messagebox.showinfo("Help Button Info",
                            "Here is a sample pop up dialog box")
        subprocess.call(["/bin/bash", "-c", "open input/SampleInput.xlsx"])

    # ABLE TO CHOOSE A .xlsx FILE TO UPLOAD; THE PATH NAME IS SAVED
    def upload_requirements(self, filename_label):
        print("Clicked Button1...")
        self.master.filename = filedialog.askopenfilename(title="Select a File", filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
        filename_label.configure(text=self.master.filename, state="active")
        self.file_name = self.master.filename
        print(self.master.filename)

    # USING THE FILE PATH NAME UPLOADED, THE .xlsx FILE IS READ AND PARSED
    # THE INPUTS ARE USED TO GENERATE A SCHEDULE
    def generate_schedule(self):
        print("Clicked Button2...")