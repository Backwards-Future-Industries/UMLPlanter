from tkinter import Tk, Label, Button


# Create the main window
root = Tk()
root.title("Hello World App")

def say_hello():
    # Create a label widget to display the message
    label = Label(root, text="Hello World!")
    label.pack()

# Create the button
button = Button(root, text="Click Me", command=say_hello)
button.pack()

# Start the main loop
root.mainloop()
