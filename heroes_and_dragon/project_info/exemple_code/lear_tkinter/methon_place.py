import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
style = ttk.Style()
style.theme_use('clam')
style.configure('1.TLabel', background='black',
                foreground='white',
                padding=40,
                width='10',
                font='Arial, 20',
                anchor='center')


label_1 = ttk.Label(root, text='Label 1',style='1.TLabel',

                    )
label_1.place(relx=0.5,rely=0.5,anchor='center')
root.mainloop()