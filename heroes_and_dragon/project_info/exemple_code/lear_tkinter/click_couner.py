import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('200x200')
root.resizable(False, False)
root.title('Click Counter')
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel',
                background='white',
                foreground='black',
                font = ('Arial',40))
count=1
def added():
    global count
    count+=1
    label.config(text=count)
label = ttk.Label(root,text='1',style='TLabel')
label.pack(anchor=tk.CENTER,pady=30)
btn = ttk.Button(root,
                 text='me',
                 command=added)
btn.pack(anchor=tk.N,)
root.mainloop()