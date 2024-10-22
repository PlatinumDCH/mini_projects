import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Tkinter Methond Pack')
root.config(bg='black')


style = ttk.Style()
style.theme_use('clam')
style.configure('1.TLabel', background='white',
                foreground='black',
                font=('Arial', 30),
                padding=30
                )
style.configure('2.TLabel', background='yellow',
                foreground='black',
                font=('Arial', 30),)
style.configure('3.TLabel', background='pink',
                font=('Arial', 30),)
style.configure('4.TLabel', background='green',
                font=('Arial', 30),)


l1 = ttk.Label(root,text='for example#1',style='1.TLabel',anchor='center')
l2 = ttk.Label(root,text='for example#2',style='2.TLabel')
l3 = ttk.Label(root,text='for example#3',style='3.TLabel')
l4 = ttk.Label(root,text='for example#4',style='4.TLabel')

l1.pack(expand=False,side='left')
# l2.pack(side='left',expand=True)
# l3.pack()
# l4.pack()


root.mainloop()
"""
parameter pack
    side
         top - defoult
         left
         right
         left
         bottom
    fill  будет ли виджет росширятся чтоб заполнить доступное пространоство
        tk.X
        tk.Y
    expand = bool   будет ли виджет занимать все доступное простарнство в контейнере
    anchor
        разположение на странице 
    padx/pady - добавляет горизонтальные и вериткальыне отступы вокрг виджета
    idax/ipady - оступы внутри виджета
    
            

"""