import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Hello World')
root.geometry('250x250')#установка росшерие для окна

def click():
    window = tk.Tk()
    window.title('New Window')
    window.geometry('250x250')

button = ttk.Button(text='Creaate new window', command=click)
button.pack(anchor=tk.CENTER,expand=1)

root.mainloop()


