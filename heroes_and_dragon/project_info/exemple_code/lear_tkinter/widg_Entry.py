import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x500')
root.title('Entry Widget')
root.config(bg='black')
root.resizable(width=False, height=False)


style = ttk.Style()
style.theme_use('clam')


e = ttk.Entry(root,show='*')
e.pack()


def added_info():
    e.insert('end',"hello")
def delete_info():
    e.delete(0,'end')

def get_info():
    label1.config(text=e.get())


style.configure('num_1.TButton', background='black', foreground='white',
                font=('Helvetica', 12, 'bold'))
btn1 = ttk.Button(root, text='Insert',style='num_1.TButton',
                  command=added_info)
btn2 = ttk.Button(root, text='delete',style='num_1.TButton',
                  command=delete_info)
btn3 = ttk.Button(root, text='get',style='num_1.TButton',
                  command=get_info)
btn1.pack()
btn2.pack()
btn3.pack()
style.configure('num_2.TLabel', background='black', foreground='white',
                font=('Helvetica', 12, 'bold'))
label1 = ttk.Label(root,style='num_2.TLabel',text='')
label1.pack()
root.mainloop()