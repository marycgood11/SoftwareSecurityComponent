#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

__author__ = "Mary Catherine Good"

# PARENT CLASS - UI OUTLINE FOR THE SCENARIOS
class ScenarioFrame(tk.Frame):
    def __init__(self, parent, controller, scenario_title, scenario_text, OPTIONS, v, next):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E6F1FF")

        # CREATE FRAMES
        title_frame = tk.Frame(self, background="#E6F1FF", width=550, pady=10)
        border_frame1 = tk.Frame(self, background="#5BA3FF", height=2, width=550)
        border_frame2 = tk.Frame(self, background="#006EFF", height=2, width=550)
        border_frame3 = tk.Frame(self, background="white", height=2, width=550)
        border_frame4 = tk.Frame(self, background="#006EFF", height=2, width=550)
        border_frame5 = tk.Frame(self, background="#5BA3FF", height=2, width=550)
        main_frame = tk.Frame(self, background="#E6F1FF", height=400, width=550)
        footer_frame = tk.Frame(self, background="#E6F1FF", height=200, width=550)

        # LAYOUT FRAMES
        title_frame.grid(row=0, column=0, sticky="nsew")
        border_frame1.grid(row=1, column=0, sticky="new")
        border_frame2.grid(row=2, column=0, sticky="new")
        border_frame3.grid(row=3, column=0, sticky="new")
        border_frame4.grid(row=4, column=0, sticky="new")
        border_frame5.grid(row=5, column=0, sticky="new")
        main_frame.grid(row=6, column=0)
        footer_frame.grid(row=7, column=0)

        # SCENARIO WIDGETS
        security_awareness_label = tk.Label(title_frame, text="Security Awareness Training", font=("Noteworthy", 30), anchor="center", background="#E6F1FF", pady=15)
        scenario1_label = tk.Label(main_frame, text=scenario_title, font=("Arial 20 bold"), wraplength=425, anchor="center", justify="left", background="#E6F1FF", pady=10)
        info_label = tk.Label(main_frame, text=scenario_text, wraplength=425, justify="left", background="#E6F1FF")
        place_holder_label1 = tk.Label(main_frame, background="#E6F1FF")
        next_button = tk.Button(footer_frame, text="Next", font=(15), command=lambda: controller.show_frame(next), highlightbackground="#5BA3FF", pady=5, width=15)

        # PLACE WIDGETS ON THE FRAME
        security_awareness_label.pack(side="top", fill="x")
        scenario1_label.pack()
        info_label.pack()
        for text, option in OPTIONS:
            b = tk.Radiobutton(main_frame, text=text, variable=v, value=option, wraplength=425, anchor="w", justify="left", background="#E6F1FF", pady=5, width=50)
            b.pack()
        place_holder_label1.pack()
        next_button.grid(row=0, column=0)

class Scenario1(ScenarioFrame, tk.Frame):
    # INITIALIZES SCENARIO 1
    def __init__(self, parent, controller):
        # SCENARIO
        scenario1_title = "Scenario 1: Password Creation"
        scenario1_text = "Alice just started a new job working at SONY Corporation.  As part of her new job, she has to create a new password to sign in and to access different applications. \nWhat rules should Alice follow when creating her new passwords?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Answer 1" , 1), ("Answer 2" , 2), ("Answer 3" , 3)]
        v = IntVar()
        # NEXT PAGE
        next = "Scenario2"

        ScenarioFrame.__init__(self, parent,controller, scenario1_title, scenario1_text, OPTIONS, v, next)


class Scenario2(tk.Frame):
    # INITIALIZES SCENARIO 2
    def __init__(self, parent, controller):
        # SCENARIO
        scenario2_title = "Scenario 2: Password Usage"
        scenario2_text = "Now even though Alice has created a new password, multiple applications require passwords.  She is thinking of using her new password, but is also considering using some passwords that she already has. This would make remembering passwords easier and she would not forget them as much.  \nWhat should Alice do?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Alice should just use her new password that she created since it follows SONY's new security policy. It is a strong password that likely will not be hacked." , 1),
        ("Alice should use a combination of her new secure password that she just created and some of her old passwords. This way she will be able to remember all of her passwords and will not have to write them down anywhere. This will make it a lot harder for hackers to guess her passwords" , 2),
        ("Alice should create a new password for each application and should not reuse any passwords. This may make it difficult to remember all of her passwords but it will be difficult for hackers to guess her passwords. To keep track of all passwords, she could use a secure password manager." , 3)]
        v = IntVar()
        # NEXT PAGE
        next = "Scenario3"

        ScenarioFrame.__init__(self, parent,controller, scenario2_title, scenario2_text, OPTIONS, v, next)


class Scenario3(tk.Frame):
    # INITIALIZES SCENARIO 3
    def __init__(self, parent, controller):
        # SCENARIO
        scenario3_title = "Scenario 3: ..."
        scenario3_text = "INFORMATION ..."
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("ANSWER 1" , 1),
        ("ANSWER 2" , 2),
        ("ANSWER 3" , 3)]
        v = IntVar()
        # NEXT PAGE
        next = "Scenario4"

        ScenarioFrame.__init__(self, parent,controller, scenario3_title, scenario3_text, OPTIONS, v, next)
