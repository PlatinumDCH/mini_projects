import tkinter as tk
from tkinter import ttk
import logic_game


def log_to_text_widget(text):
    text_widget.insert(tk.END, text + '\n')
    text_widget.see(tk.END)

root = tk.Tk()
root.geometry('650x500')

style = ttk.Style()
style.theme_use('clam')
style.configure('custom.Horizontal.TProgressbar',
                background='blue',
                troughcolor='gray',
                thickness=20)
frame_bar = tk.Frame(root,
                     bg='lightgray',
                     width=400, height=40)
label_lvl = tk.Label(frame_bar,
                     bg='black',
                     fg='white',
                     text='1',
                     font=('Arial', 14),
                     width=10,
                     height=2)
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(frame_bar,
                               orient=tk.HORIZONTAL,
                               style='custom.Horizontal.TProgressbar',
                               length=300,
                               mode='determinate',
                               variable=progress_var,
                               maximum=100)
buttom_attack = tk.Button(root,
                          text='Attack',
                          font=('Arial', 40),
                          width=20,
                          command=lambda :fight()
                          )
frame_attack_info = tk.Frame(root,
                             bg='lightgray',
                             width=450, height=300)
text_widget = tk.Text(frame_attack_info,
                      wrap=tk.WORD,
                      width=61,
                      height=23,
                      )
scrollbar = tk.Scrollbar(frame_attack_info,
                         command=text_widget.yview,


                         )
frame_bar.place(x=90, y=5)
label_lvl.place(x=3, y=3)
progress_bar.place(x=95, y=15)
buttom_attack.place(x=50, y=400)
frame_attack_info.place(x=70,y=70)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

obj_h = logic_game.Hero('Dima', 15, 100)
monsters = list(logic_game.tuple_monsters)
obj_m = None


def fight():
    global obj_m
    if obj_m is None or not obj_m.is_alive():
        if monsters:
            current_monster = monsters.pop(0)
            obj_m = logic_game.Monster(*current_monster)
            log_to_text_widget(f'New Monster: {obj_m.name}')
        else:
            log_to_text_widget("All monsters defeated!")
            return

    hero_log_attack = obj_h.initialized_fighter(obj_m)
    log_to_text_widget(hero_log_attack)
    log_to_text_widget('--------')

    if not obj_h.is_alive():
        log_to_text_widget(f'{obj_h.name} is dead...')
        return

    if not obj_m.is_alive():
        log_to_text_widget(f'{obj_m.name} is dead!')
        obj_h.change_lvl()
        label_lvl.configure(text=f'{obj_h.lvl}')
        log_to_text_widget(f'{obj_h.name} level up')
        log_to_text_widget('@@@')
        log_to_text_widget(f'{obj_h.get_info()}')
    else:
        monster_log_attack=obj_m.initialized_fighter(obj_h)
        log_to_text_widget(monster_log_attack)
        if not obj_h.is_alive():
            log_to_text_widget(f'{obj_h.name} is dead ... ')
            return

root.mainloop()