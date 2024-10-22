import tkinter as tk
from tkinter import ttk
def click():
    print('hello conslo dima')

def ct():
    """
    background - цвет фона виджета
    foreground - цвет текста виджета
    font - фришт текста в виджете
    padding - внутренний отступы(в пикселях_
        padding(int(x),int(y))
    borderwith  - ширина границы вокруг виджета
    relief - стиль границы виджета
        flat
        raised
        sunken
        solid
        ridge
        groove

    anchor - определяеть где содержимое будет нахожиться внутри виджета
        n
        s
        e
        w
        ne
        nw
        se
        sw
        center
    highlightthickness - толщина обвожки виджета которая появл при его фокусе
    cursor
    image
    compound
    highlightcolor
    takefocus = bool

            :return:
    """
    style = ttk.Style()
    style.configure('Custom.TButton',
                    font=('Arial',20,'italic'),
                    foreground='black',
                    background='light pink',
                    width=10,

                    )
    # для изменение параметров кнопки во время действий
    # active. pressed, disable
    style.map('Custom.TButton',
              foreground=[('pressed', 'black')],
              background=[('pressed','blue')],)

    style.configure('Custom.TEntry',
                    font=('Arial',20,'italic'),
                    foreground='black',
                    background='white',)
    style.configure('Custom.TLabel',
                    font=('Arial',20,'italic'),
                    foreground='black',
                    background='light blue',)