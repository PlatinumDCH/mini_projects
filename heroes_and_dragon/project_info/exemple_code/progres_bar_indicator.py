import tkinter as tk
from tkinter import ttk

from project_info.exemple_code.progress_bar import progress_bar


def start_progress():
    progress_bar['value'] = 0
    root.after(100,update_progress)


def update_progress():
    progress_bar.step(5)
    if progress_bar['value'] <100:
        root.after(100,update_progress)


root = tk.Tk()
root.title('Progres bar indicator')

progress_bar = ttk.Progressbar(root,
                               orient='horizontal',
                               length=300,
                               mode='determinate')
progress_bar.pack(pady=20)

start_button = tk.Button(root,
                         text='Start',
                         command=start_progress)
start_button.pack(pady=20)

root.mainloop()