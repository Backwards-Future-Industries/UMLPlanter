from tkinter import Frame

class dls_zone(Frame):
    def __init__(self, master, global_background, border_thickness, border_color):
        super().__init__(
            master,
            bg = global_background,
            height = 1024,
            width = 450,
            highlightthickness = border_thickness,
            highlightbackground = border_color,
            relief = "ridge"
            )