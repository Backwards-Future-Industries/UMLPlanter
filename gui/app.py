from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#global variables
globalbackground = "#FFFFFF"
borderthinkness = 5

#creating the window
window = Tk()
window.geometry("1440x1024")
window.configure(bg = globalbackground)
window.title("UMLPlanter")

#creating and configuring the canvas
canvas1 = Canvas(
    window,
    bg = globalbackground,
    height = 480,
    width = 250,
    highlightthickness = borderthinkness,
    relief = "ridge"
)
canvas2 = Canvas(
    window,
    bg = globalbackground,
    height = 544,
    width = 250,
    highlightthickness = borderthinkness,
    relief = "ridge"
)
canvas3 = Canvas(
    window,
    bg = globalbackground,
    height = 1024,
    width = 740,
    highlightthickness = borderthinkness,
    relief = "ridge"
)
canvas4 = Canvas(
    window,
    bg = globalbackground,
    height = 1024,
    width = 450,
    highlightthickness = borderthinkness,
    relief = "ridge"
)

#putting the canvas on the window
canvas1.place(x = 0, y = 0)
canvas2.place(x = 0, y = 480)
canvas3.place(x = 250, y = 0)
canvas4.place(x = 990, y = 0)

#buttom 1
image_1 = PhotoImage(file="gui/assets/image_1.png")
b = Button(canvas1, image=image_1, command=window.quit, bg = globalbackground)
b.place(x=40, y=30)

#buttom 2
image_2 = PhotoImage(file="gui/assets/image_2.png")
b2 = Button(canvas1, image=image_2, command=window.quit, bg = globalbackground)
b2.place(x=40, y=250)

#start the application
window.resizable(False, False)
window.mainloop()
