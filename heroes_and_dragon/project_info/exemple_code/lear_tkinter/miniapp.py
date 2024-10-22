import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime

temp = 0
after_id = ''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label_1.config(text=f_temp)
    temp += 1

def sterted():
    buttonStart.pack_forget()
    buttonStop.pack()
    tick()

def stop_tick():
    buttonStop.pack_forget()
    buttonContinue.pack()
    buttonRestart.pack()
    root.after_cancel(after_id)

def continue_tick():
    buttonContinue.pack_forget()
    buttonRestart.pack_forget()
    buttonStop.pack()
    tick()

def reset_tick():
    global temp
    temp = 0
    label_1.config(text='00:00')
    buttonContinue.pack_forget()
    buttonRestart.pack_forget()
    buttonStart.pack()


root = tk.Tk()
root.title('Mini App')
root.resizable(False, False)
root.geometry('300x200')

style = ttk.Style()
style.theme_use('clam')
style.configure('1.TLabel',
                font='Arial 30',
                width=10,
                anchor='center',
                background='light blue',
                foreground='black'
                )

style.configure('B.TButton',
                font='Arial 30',
                background='gray',
                foreground='yellow',
                # anchor='center',
                 )

label_1 = ttk.Label(root,style='1.TLabel',
                text='00:00')
buttonStart = ttk.Button(root,style='B.TButton',
                         text='Start',
                         command=sterted)
buttonStop = ttk.Button(root,style='B.TButton',
                        text='Stop',
                        command=stop_tick)
buttonContinue = ttk.Button(root,style='B.TButton',
                            text='Continue',
                            command=continue_tick)
buttonRestart = ttk.Button(root,style='B.TButton',
                         text='Restart',
                           command=reset_tick)

label_1.pack(pady=15)

buttonStart.pack()

root.mainloop()