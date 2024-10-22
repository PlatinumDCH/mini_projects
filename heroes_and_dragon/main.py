import time
import tkinter as tk
from tkinter import ttk
import logic_game
import time

variable = 25
const_lvl = 1


def game_loop():
    global variable,current_monster, index
    # Если герой жив и монстр ещё жив
    if obj_h.is_alive() and current_monster.is_alive():
        obj_h.initialized_fighter(current_monster)
        if not current_monster.is_alive():
            current_monster.initialized_fighter(obj_h)
            if not obj_h.is_alive():
                print(f'{obj_h.name} is dead...',flush=True)
                time.sleep(1)
            else:
                print(f'{current_monster.name} is dead!',flush=True)
                time.sleep(1)
                obj_h.change_lvl()
                label_lvl.configure(text=f'{obj_h.lvl}')
                print(f'{obj_h.name} level up!',flush=True)
                time.sleep(1)
                label_lvl.configure(text=f'HP: {obj_h.hp}')
        root.after(1000, game_loop)
    else:
        if index < len(logic_game.tuple_monsters) - 1:
            index += 1
            current_monster = logic_game.Monster(*logic_game.tuple_monsters[index])
            root.after(1000, game_loop)


root = tk.Tk()
root.geometry('650x500')
style = ttk.Style()
style.theme_use('clam')
style.configure('custom.Horizontal.TProgressbar',
                background='blue',
                troughcolor='gray',
                thickness=20,
                )

frame_bar = tk.Frame(root,
                     bg='lightgray',
                     width=400,height=40)

label_lvl = tk.Label(frame_bar,
                     bg='black',
                     fg='white',
                     text='1',
                     font=('Arial', 14),
                     width=10,
                     height=2,)
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(frame_bar,
                               orient=tk.HORIZONTAL,
                               style='custom.Horizontal.TProgressbar',
                               length=300,
                               mode='determinate',
                               variable=progress_var,
                               maximum = 100)


frame_bar.place(x=5, y=5)
label_lvl.place(x=3, y=3)
progress_bar.place(x=95, y=15)

if __name__ == '__main__':
    obj_h = logic_game.Hero('Dima', 15, 100)
    index = 0
    current_monster = logic_game.Monster(*logic_game.tuple_monsters[index])
    root.after(1000, game_loop)
    root.mainloop()
