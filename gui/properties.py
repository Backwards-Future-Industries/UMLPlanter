from tkinter import Frame

class properties(Frame):
    def __init__(self, master, global_background, border_thickness, border_color):
        super().__init__(
            master,
            bg = global_background,
            height = 544,
            width = 250,
            highlightthickness = border_thickness,
            highlightbackground = border_color,
            relief = "ridge"
        )