#!/usr/bin/env python3
"""
Starts UI
"""
import tkinter as tk

from front_end import homescreen

__author__ = "Mary Catherine Good"

if __name__ == '__main__':
    root = tk.Tk()
    app = homescreen.Home(root)
    root.mainloop()
