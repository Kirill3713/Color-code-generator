import customtkinter as ctk
import tkinter as tk

from color_frame import ColorFrame


def save_colors():
    with open("My colors.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(f"{cf1.colorcode_output.get()}\n")
        txt_file.write(f"{cf2.colorcode_output.get()}\n")
        txt_file.write(f"{cf3.colorcode_output.get()}\n")
        txt_file.write(f"{cf4.colorcode_output.get()}\n")

def load_colors():
    try:
        with open("My colors.txt", "r", encoding="utf-8") as txt_file:
            list_of_colors = []
            for line in txt_file:
                list_of_colors.append(line)
            cf1.set_color(list_of_colors[0].replace("\n", ""))
            cf2.set_color(list_of_colors[1].replace("\n", ""))
            cf3.set_color(list_of_colors[2].replace("\n", ""))
            cf4.set_color(list_of_colors[3].replace("\n", ""))
    except FileNotFoundError:
        print("Сохраненные цвета не найдены.")


root = ctk.CTk()

menu = tk.Menu(root)
root.configure(menu=menu)
menu.add_command(label="Сохранить", command=save_colors)
menu.add_command(label="Загрузить сохраненные цвета", command=load_colors)

cf1 = ColorFrame(root)
cf1.grid(column = 0, row = 0)

cf2 = ColorFrame(root)
cf2.grid(column = 1, row = 0)

cf3 = ColorFrame(root)
cf3.grid(column = 2, row = 0)

cf4 = ColorFrame(root)
cf4.grid(column = 3, row = 0)



root.mainloop()