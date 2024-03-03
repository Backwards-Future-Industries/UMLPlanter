from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
from canvas import canvas
from element_selector import element_selector
from properties import properties
from dls_zone import dls_zone

#global variables
global_background = "#FFFFFF"
border_thickness = 5
border_color = "black"

#creating the window
window = Tk()
window.geometry("1440x1024")
window.configure(bg = global_background)
window.title("UMLPlanter")

#creating and configuring the canvas
frame1 = element_selector(window, global_background, border_thickness, border_color)
frame2 = properties(window, global_background, border_thickness, border_color)
canvas = canvas(window, global_background, border_thickness, border_color)
frame4 = dls_zone(window, global_background, border_thickness, border_color)

#putting the canvas on the window
frame1.place(x = 0, y = 0)
frame2.place(x = 0, y = 480)
canvas.place(x = 250, y = 0)
frame4.place(x = 990, y = 0)

#creating a box on canvas
def place_box():
    #creating the box
    canvas.create_text(
        10,
        10,
        text="Hello, world!",
        tags = "move")
    

#creating an arrow on canvas
def place_arrow():
    #creating the arrow
    canvas.create_line(
        100, 100, 200, 200,
        fill = "black",
        width = 2,
        arrow = "last",
        tags = "move")

#buttom 1
image_1 = PhotoImage(file="gui/assets/image_1.png")
b = Button(frame1, image=image_1, command=place_box, bg = global_background)
b.place(x=40, y=30)

#buttom 2
image_2 = PhotoImage(file="gui/assets/image_2.png")
b2 = Button(frame1, image=image_2, command=place_arrow, bg = global_background)
b2.place(x=40, y=250)

#cloes the application on escape
window.bind('<Escape>',lambda x: window.quit())
#start the application
window.resizable(False, False)
window.mainloop()
