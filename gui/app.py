from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")

canvas1 = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 250,
    bd = 0,
    highlightthickness = 5,
    relief = "ridge"
)

canvas2 = Canvas(
    window,
    bg = "#FFFFFF",
    height = 544,
    width = 250,
    bd = 0,
    highlightthickness = 5,
    relief = "ridge"
)

canvas3 = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 740,
    bd = 0,
    highlightthickness = 5,
    relief = "ridge"
)

canvas4 = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 450,
    bd = 0,
    highlightthickness = 5,
    relief = "ridge"
)

canvas1.place(x = 0, y = 0)
canvas2.place(x = 0, y = 480)
canvas3.place(x = 250, y = 0)
canvas4.place(x = 690, y = 0)

image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
canvas1.create_image(
    121.0,
    115.0,
    image=image_1
)

image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
canvas1.create_image(
    122.0,
    272.99999999999994,
    image=image_2
)
window.resizable(False, False)
window.mainloop()
