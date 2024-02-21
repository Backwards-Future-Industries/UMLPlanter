from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
from canvas import canvas

#global variables
globalbackground = "#FFFFFF"
borderthinkness = 5

#creating the window
window = Tk()
window.geometry("1440x1024")
window.configure(bg = globalbackground)
window.title("UMLPlanter")

#creating and configuring the canvas
frame1 = Frame(
    window,
    bg = globalbackground,
    height = 480,
    width = 250,
    highlightthickness = borderthinkness,
    relief = "ridge"
)
frame2 = Frame(
    window,
    bg = globalbackground,
    height = 544,
    width = 250,
    highlightthickness = borderthinkness,
    relief = "ridge"
)
canvas = canvas(window, globalbackground, borderthinkness)

frame4 = Frame(
    window,
    bg = globalbackground,
    height = 1024,
    width = 450,
    highlightthickness = borderthinkness,
    relief = "ridge"
)

#putting the canvas on the window
frame1.place(x = 0, y = 0)
frame2.place(x = 0, y = 480)
canvas.place(x = 250, y = 0)
frame4.place(x = 990, y = 0)

#creating a box on canvas3
def place_box():
    #creating the box
    canvas.create_rectangle(
        100, 100, 200, 200,
        fill = "white",
        outline = "black",
        width = 2,
        tags = "move")


#buttom 1
image_1 = PhotoImage(file="gui/assets/image_1.png")
b = Button(frame1, image=image_1, command=place_box, bg = globalbackground)
b.place(x=40, y=30)

#buttom 2
image_2 = PhotoImage(file="gui/assets/image_2.png")
b2 = Button(frame1, image=image_2, command=window.quit, bg = globalbackground)
b2.place(x=40, y=250)

#start the application
window.resizable(False, False)
window.mainloop()
