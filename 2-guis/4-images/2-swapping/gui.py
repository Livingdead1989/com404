from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # Loading Resources
        self.cactus_image = PhotoImage(file="4-images/2-swapping/cactus.gif")
        self.cactus_with_name_image = PhotoImage(file="4-images/2-swapping/cactus_with_name.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()
        self.__add_cactus_image_label()
        self.__add_flip_button()

    
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0)
        self.heading_label.configure(
            font="Arial 22",
            text="Cactus Leaves"
        )
        
    def __add_cactus_image_label(self):
        #create
        self.cactus_image_label = Label()
        #place
        self.cactus_image_label.grid(row=1)
        #style
        self.cactus_image_label.configure(
            image=self.cactus_image,
            height=300,
            width=400
        )

    def __add_flip_button(self):
        #create
        self.flip_button = Button()
        #place
        self.flip_button.grid(row=2)
        #style
        self.flip_button.configure(
            text="FLIP",
            pady=10,
            padx=40
        )
    
    # Binds the event ButtonRelease-1 (left mouse) to an event called flip_button_clicked
        self.flip_button.bind("<ButtonRelease-2>", self.__flip_right_button_clicked)
        self.flip_button.bind("<ButtonRelease-1>", self.__flip_left_button_clicked)
    
    # event handler
    def __flip_left_button_clicked(self, event):
        self.cactus_image_label.configure(
            image = self.cactus_image
        )
    def __flip_right_button_clicked(self, event):
        self.cactus_image_label.configure(
            image = self.cactus_with_name_image
        )

# Create an object of the Gui class when this module is executed
# This is for convenience. Normally the following would be in the main.py file.
# The if statement simply makes sure that the window is displayed when this file is run
# directly as opposed to being imported into another class.
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	