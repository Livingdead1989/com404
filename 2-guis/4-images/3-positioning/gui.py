from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # Loading Resources
        self.map_image = PhotoImage(file="4-images/3-positioning/map.gif")
        self.bus_image = PhotoImage(file="4-images/3-positioning/bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_map_frame()
        self.__add_map_image_label()
        self.__add_bus_image_label()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0)
        self.heading_label.configure(
            font="Arial 22",
            text="Bus Journey"
        )

    def __add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1)
        self.map_frame.configure(
            width=745, 
            height=570
            )
        
    def __add_map_image_label(self):
        #create
        self.map_image_label = Label(self.map_frame)
        #place
        self.map_image_label.place(x=0, y=0)
        #style
        self.map_image_label.configure(
            image=self.map_image,
            height=540,
            width=740
        )
    
    def __add_bus_image_label(self):
        #create
        self.bus_image_label = Label(self.map_frame)
        #place
        self.bus_image_label.place(x=10, y=10)
        #style
        self.bus_image_label.configure(
            image=self.bus_image,
            height=68,
            width=128
        )
        self.bus_image_label.bind("<B1-Motion>", self.__callback)

    def __callback(self, event):

        #messagebox.showinfo("Bus Journey Gui", "Mouse X is " + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse Y is " + str(event.y))

        #print "Mouse at " + str(event.x) + "x " + str(event.y)

        self.bus_image_label.place(
            x=event.x, 
            y=event.y)

# Create an object of the Gui class when this module is executed
# This is for convenience. Normally the following would be in the main.py file.
# The if statement simply makes sure that the window is displayed when this file is run
# directly as opposed to being imported into another class.
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	