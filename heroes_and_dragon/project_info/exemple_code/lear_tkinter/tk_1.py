import tkinter as tk
from tkinter import ttk
import comad_tkinter

root = tk.Tk()

# window conf.
root.title("Test Application")
root.geometry("500x500")
root.resizable(False, False)

# theme ttk use interface
style = ttk.Style()
style.theme_use('clam')

# config icon apps
root.iconbitmap('icon_2.png')

# configure fort apps
# root['bg'] = 'lightblue'
root.config(bg='light yellow')

def update_label():
    entered_text = e.get()
    l.config(text=entered_text)


e = ttk.Entry(root)
e.pack(pady=10)

l = tk.Label(root,
              text='Здесь будет твой текст',
              width=25,
              height=15)
l.pack(pady=10)

btn = tk.Button(root,
                 text='обновить лейбл',
                 command=update_label,
                 width=10,
                 height=3,

                )
btn.pack(anchor=tk.N)
root.mainloop()
