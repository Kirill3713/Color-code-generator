import customtkinter as tk

class ColorFrame(tk.CTkFrame):
    def __init__(self, container) -> None:
        super().__init__(container)
        self.red_value, self.green_value, self.blue_value = '00', '00', '00'
        self.selected_color = "#" + self.red_value + self.green_value + self.blue_value
        
        
        self.r_slider = tk.CTkSlider(self, from_=0, to=255, command= lambda value: self.get_value(value, "red"))
        self.r_slider.grid(row = 2, column = 1, padx = (5, 10), pady = 10)
        self.r_slider.set(0)

        self.red_label = tk.CTkLabel(self, text_color="red", text="R", font = ("Jokerman", 22))
        self.red_label.grid(row = 2, column = 0, padx=(10, 5), pady=10)
        
        
        self.g_slider = tk.CTkSlider(self, from_=0, to=255, command= lambda value: self.get_value(value, "green"))
        self.g_slider.grid(row = 3, column = 1, padx = (5, 10), pady = 10)
        self.g_slider.set(0)

        self.green_label = tk.CTkLabel(self, text_color="green", text="G", font = ("Jokerman", 22))
        self.green_label.grid(row = 3, column = 0, padx=(10, 5), pady=10)
        
        
        self.b_slider = tk.CTkSlider(self, from_=0, to=255, command= lambda value: self.get_value(value, "blue"))
        self.b_slider.grid(row = 4, column = 1, padx = (5, 10), pady = 10)
        self.b_slider.set(0)

        self.blue_label = tk.CTkLabel(self, text_color="blue", text="B", font = ("Jokerman", 22))
        self.blue_label.grid(row = 4, column = 0, padx=(10, 5), pady=10)
        
        
        self.color_preview = tk.CTkLabel(self, bg_color=self.selected_color, width=100, height=100, text=None)
        self.color_preview.grid(column=0, row=0, padx=10, pady=10, columnspan = 2)

        self.colorcode_output = tk.CTkEntry(self, font=("Jokerman", 20))
        self.colorcode_output.grid(column=0, columnspan=2, row = 1, padx=(10, 0), pady=10)
        
        self.set_color("#000000")

        self.colorcode_output.bind("<Return>", self.call_of_set_color)

    def call_of_set_color(self, variable_for_2nd_arg):
        self.color = str(self.colorcode_output.get())
        self.set_color(color=self.color)
    def get_value(self, value, color):

        value = hex(int(value)).replace("0x", "")
        value = value.rjust(2, "0")
        if color == "red":
            self.red_value = value
        elif color == "green":
            self.green_value = value
        elif color == "blue":
            self.blue_value = value
        self.selected_color = "#" + self.red_value + self.green_value + self.blue_value
        self.selected_color = self.selected_color
        self.color_preview.configure(bg_color=self.selected_color)
        self.colorcode_output.delete(0, "end")
        self.colorcode_output.insert(0, self.selected_color)
    def get_color(self):
        return self.selected_color
    def set_color(self, color):
        color = color.strip()
        self.color_dict = {
            "red": "#FF0000",
            "orange": "#FF0F00",
            "yellow": "#FFFF00",
            "green": "#00FF00",
            "cyan": "#00FFFF",
            "blue": "#0000FF",
            "purple": "#FF00FF",
            "black": "#000000",
            "white": "#FFFFFF",
            "grey": "#808080",
            "pink": "#ff53af",
            "sero-buro-malinovyy": "#774C52"
        }
        if color in self.color_dict.keys():
            self.selected_color = self.color_dict[color]
        else:
            self.selected_color = color
        self.red_value = self.selected_color[1:3]
        self.green_value = self.selected_color[3:5]
        self.blue_value = self.selected_color[5:7]

        self.color_preview.configure(bg_color = self.selected_color)
        self.colorcode_output.delete(0, "end")
        self.colorcode_output.insert(0, self.selected_color)
        self.r_slider.set(int(self.red_value, 16))
        self.g_slider.set(int(self.green_value, 16))
        self.b_slider.set(int(self.blue_value, 16))
if __name__ ==  "__main__":
    root = tk.CTk()
    a = ColorFrame(root)
    root.resizable(0, 0)
    a.grid(row = 0, column = 0)
    a.set_color("yellow")
    root.mainloop()