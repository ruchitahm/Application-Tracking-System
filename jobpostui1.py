import os
import subprocess
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Resumex")
win.resizable(False,False)
ttk.Label(win, text = "Enter JobPost Here").grid(column=0, row=0)
jobpost=tk.StringVar()
jobpost_entered=ttk.Entry(win, width=30, textvariable=jobpost)
jobpost_entered.grid(column=0, row=1)
jobpost_entered.focus()
def click():
    with open("op.txt","w")as text_file:
     print(jobpost.get(), file=text_file)
     subprocess.Popen("jobpost1.py 1", shell=True)
action=ttk.Button(win, text="Click", command=click)
action.grid(column=1, row=1)

win.mainloop()
