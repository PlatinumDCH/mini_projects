import tkinter as tk
from tkinter import ttk
import time


def start_progress():
    progress_bar['value'] = 0
    for i in range(101):
        progress_bar['value'] = i
        root.update_idletasks()# обновлняем интерфейс
        time.sleep(0.05) #симуляция длительности задачи


root = tk.Tk()
root.title('Progress Bar exemple')

progress_bar = ttk.Progressbar(root, orient = 'horizontal',length=300,mode='determinate')
progress_bar.pack(pady=20)

start_button = tk.Button(root,text='Start',command=start_progress)
start_button.pack(pady=20)
root.mainloop()