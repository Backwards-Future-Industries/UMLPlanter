from tkinter import Canvas

class canvas(Canvas):
    def __init__(self, window, global_background, border_thickness, border_color):
        super().__init__(
            window,
            bg = global_background,
            height = 1024,
            width = 740,
            highlightthickness = border_thickness,
            highlightbackground = border_color,
            relief = "ridge",
        )
        self.place(x = 250, y = 0)

        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.tag_bind("move", "<ButtonPress-1>", self.drag_start)
        self.tag_bind("move", "<ButtonRelease-1>", self.drag_stop)
        self.tag_bind("move", "<B1-Motion>", self.drag)

    #https://stackoverflow.com/a/6789351
    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = self.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y