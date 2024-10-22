import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400')
root.title('Minigame')
root.resizable(False, False)
root.configure(bg='black')

style = ttk.Style()
style.theme_use('default')

style.configure('TButton',
                background='black',
                fg = 'white',
                font = ('Arial', 20,),
                )
style.configure('TLabel',
                background='white',
                fg = 'white',
                font = ('Arial', 20,),
                )

Labeltext = ttk.Label(root,
                          text='',
                          style='TLabel')
Labeltext.place(y=200,x=200)
root.mainloop()
