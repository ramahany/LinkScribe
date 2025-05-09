import tkinter as tk
import ttkbootstrap as ttk
from AutomationApp import AutomationApp

if __name__ == '__main__':
    window = ttk.Window(title='test place', themename="darkly",
                        resizable=[False, False], alpha=1)
    window.geometry('1200x900')

    AutomationApp(window)
    window.mainloop()
