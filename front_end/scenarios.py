#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

__author__ = "Mary Catherine Good"

class Scenario1(tk.Frame):
    # INITIALIZES SCENARIO 1
    def __init__(self, parent, controller):
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
        scenario1_label = tk.Label(main_frame, text="Scenario 1 - ...", wraplength=425, justify="left", background="#E6F1FF", pady=20)
        place_holder_label1 = tk.Label(main_frame, background="#E6F1FF")
        back_button = tk.Button(footer_frame, text="Back", font=(15), command=lambda: controller.show_frame("HomePage"), highlightbackground="#5BA3FF", pady=5, width=15)
        place_holder_label2 = tk.Label(footer_frame, background="#E6F1FF")
        next_button = tk.Button(footer_frame, text="Next", font=(15), command=lambda: controller.show_frame("Scenario2"), highlightbackground="#5BA3FF", pady=5, width=15)

        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Answer 1" , 1), ("Answer 2" , 2), ("Answer 3" , 3)]
        v = IntVar()

        # PLACE WIDGETS ON THE FRAME
        security_awareness_label.pack(side="top", fill="x")
        scenario1_label.pack()
        for text, option in OPTIONS:
            b = tk.Radiobutton(main_frame, text=text, variable=v, value=option, wraplength=425, anchor="w", justify="left", background="#E6F1FF", pady=5, width=50)
            b.pack()
        place_holder_label1.pack()
        back_button.grid(row=0, column=0)
        place_holder_label2.grid(row=0, column=1)
        next_button.grid(row=0, column=2)

class Scenario2(tk.Frame):
    # INITIALIZES SCENARIO 2
    def __init__(self, parent, controller):
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
        scenario_label = tk.Label(main_frame, text="Scenario 2 - ...", wraplength=425, justify="left", background="#E6F1FF", pady=20)
        place_holder_label1 = tk.Label(main_frame, background="#E6F1FF")
        back_button = tk.Button(footer_frame, text="Back", font=(15), command=lambda: controller.show_frame("Scenario1"), highlightbackground="#5BA3FF", pady=5, width=15)
        place_holder_label2 = tk.Label(footer_frame, background="#E6F1FF")
        next_button = tk.Button(footer_frame, text="Next", font=(15), command=lambda: controller.show_frame("Scenario3"), highlightbackground="#5BA3FF", pady=5, width=15)

        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Answer 1" , 1), ("Answer 2" , 2), ("Answer 3" , 3)]
        v = IntVar()

        # PLACE WIDGETS ON THE FRAME
        security_awareness_label.pack(side="top", fill="x")
        scenario_label.pack()
        for text, option in OPTIONS:
            b = tk.Radiobutton(main_frame, text=text, variable=v, value=option, wraplength=425, anchor="w", justify="left", background="#E6F1FF", pady=5, width=50)
            b.pack()
        place_holder_label1.pack()
        back_button.grid(row=0, column=0)
        place_holder_label2.grid(row=0, column=1)
        next_button.grid(row=0, column=2)


class Scenario3(tk.Frame):
    # INITIALIZES SCENARIO 2
    def __init__(self, parent, controller):
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
        scenario_label = tk.Label(main_frame, text="Scenario 3 - ...", wraplength=425, justify="left", background="#E6F1FF", pady=20)
        place_holder_label1 = tk.Label(main_frame, background="#E6F1FF")
        back_button = tk.Button(footer_frame, text="Back", font=(15), command=lambda: controller.show_frame("Scenario2"), highlightbackground="#5BA3FF", pady=5, width=15)
        place_holder_label2 = tk.Label(footer_frame, background="#E6F1FF")
        #next_button = tk.Button(footer_frame, text="Next", font=(15), command=lambda: controller.show_frame("Scenario4"), highlightbackground="#5BA3FF", pady=5, width=15)

        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Answer 1" , 1), ("Answer 2" , 2), ("Answer 3" , 3)]
        v = IntVar()

        # PLACE WIDGETS ON THE FRAME
        security_awareness_label.pack(side="top", fill="x")
        scenario_label.pack()
        for text, option in OPTIONS:
            b = tk.Radiobutton(main_frame, text=text, variable=v, value=option, wraplength=425, anchor="w", justify="left", background="#E6F1FF", pady=5, width=50)
            b.pack()
        place_holder_label1.pack()
        back_button.grid(row=0, column=0)
        place_holder_label2.grid(row=0, column=1)
        #next_button.grid(row=0, column=2)


if __name__ == "__main__":
    app = UI_Setup()
    app.mainloop()
