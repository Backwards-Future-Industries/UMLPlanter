from tkinter import Frame

class dls_zone(Frame):
    def __init__(self, master, globalbackground, borderthinkness):
        super().__init__(
            master,
            bg = globalbackground,
            height = 1024,
            width = 450,
            highlightthickness = borderthinkness,
            relief = "ridge"
            )