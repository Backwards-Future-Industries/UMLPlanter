from tkinter import Frame

class element_selactor(Frame):
    def __init__(self, master, globalbackground, borderthinkness):
        super().__init__(
            master,
            bg = globalbackground,
            height = 480,
            width = 250,
            highlightthickness = borderthinkness,
            relief = "ridge"
        )