import tkinter as tk

count = 0
def add_line():
    global count
    count += 1
    new_line = f"New line added dynamically {count}.\n"
    text_widget.insert(tk.END, new_line)
    text_widget.see(tk.END)  # Прокручивает виджет до конца

root = tk.Tk()
root.geometry('300x200')

text_widget = tk.Text(root,
                      wrap=tk.WORD,
                      height=10,
                      width=40,
                      background='lightblue',
                      foreground='black',
                      font=('Arial', 12))

text_widget.pack(pady=20)

# Кнопка для добавления новой строки
add_button = tk.Button(root, text="Add Line", command=add_line)
add_button.pack()

root.mainloop()
