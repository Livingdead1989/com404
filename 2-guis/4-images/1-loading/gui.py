from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # Loading Resources
        self.ambulance_image = PhotoImage(file="4-images/1-loading/ambulance.gif")
        self.bike_image = PhotoImage(file="4-images/1-loading/bike.gif")
        self.plane_image = PhotoImage(file="4-images/1-loading/plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0,columnspan=3)
        self.heading_label.configure(
            font="Arial 22",
            text="TRANSPORT"
        )
        
    def __add_ambulance_image_label(self):
        #create
        self.ambulance_image_label = Label()
        #place
        self.ambulance_image_label.grid(row=1, column=0)
        #style
        self.ambulance_image_label.configure(
            image=self.ambulance_image,
            height=60,
            width=60
        )

    def __add_bike_image_label(self):
        #create
        self.bike_image_label = Label()
        #place
        self.bike_image_label.grid(row=1, column=1)
        #style
        self.bike_image_label.configure(
            image=self.bike_image,
            height=60,
            width=60
        )
 
    def __add_plane_image_label(self):
        #create
        self.plane_image_label = Label()
        #place
        self.plane_image_label.grid(row=1, column=2)
        #style
        self.plane_image_label.configure(
            image=self.plane_image,
            height=60,
            width=60
        )

# Create an object of the Gui class when this module is executed
# This is for convenience. Normally the following would be in the main.py file.
# The if statement simply makes sure that the window is displayed when this file is run
# directly as opposed to being imported into another class.
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	