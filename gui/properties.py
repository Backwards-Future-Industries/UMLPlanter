from tkinter import Frame

class properties(Frame):
    def __init__(self, master, globalbackground, borderthinkness):
        super().__init__(
            master,
            bg = globalbackground,
            height = 544,
            width = 250,
            highlightthickness = borderthinkness,
            relief = "ridge"
        )