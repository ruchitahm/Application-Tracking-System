import os
import subprocess
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Resumex")
win.resizable(False,False)
ttk.Label(win, text = "Enter technical Skills Here").grid(column=0, row=0)
techskills=tk.StringVar()
techskills_entered=ttk.Entry(win, width=30, textvariable=techskills)
techskills_entered.grid(column=0, row=1)
techskills_entered.focus()
def click():
    with open("op3.txt","w")as text_file:
        print(techskills.get(), file=text_file)
        print(techskills.get())
    subprocess.Popen("candidate1.py 1", shell=True)
action=ttk.Button(win, text="Click", command=click)
action.grid(column=1, row=1)
win.mainloop()
