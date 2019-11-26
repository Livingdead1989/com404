from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # Loading Resources
        self.cross_image = PhotoImage(file="4-images/3-positioning/map.gif")
        self.tick_image = PhotoImage(file="4-images/3-positioning/bus.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.__add_heading_label()

        self.__add_name_label()
        self.__add_name_entry()
        self.__add_name_check_label()

        self.__add_passport_label()
        self.__add_passport_entry()
        self.__add_passport_check_label()

        self.__add_nights_label()
        self.__add_nights_entry()
        self.__add_nights_check_label()

        self.__add_checkin_button()

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, columnspan=3)
        self.heading_label.configure(
            font="Arial 22",
            text="Hotel Check-In"
        )

    def __add_name_label(self):
        self.name_label = Label()
        self.name_label.grid(row=1,column=0)
        self.name_label.configure(
            text="Name"
        )

    def __add_name_entry(self):
        self.name_entry = Entry()
        self.name_entry.grid(row=1,column=1)
        self.name_entry.configure(
            width=20
        )
        self.name_entry.bind("<FocusOut>", self.__name_callback)

    def __name_callback(self, event):
        if(len(self.name_entry.get()) > 0):
            self.name_check_label.configure(bg="#33cc33")
        else:
            self.name_check_label.configure(bg="#ff0000")

    def __add_name_check_label(self):
        self.name_check_label = Label()
        self.name_check_label.grid(row=1,column=2)
        self.name_check_label.configure(
            width=2,
            height=1,
            bd=4,
            bg="#ccc"
        )

    def __add_passport_label(self):
        self.passport_label = Label()
        self.passport_label.grid(row=2,column=0)
        self.passport_label.configure(
            text="Passport Number"
        )

    def __add_passport_entry(self):
        self.passport_entry = Entry()
        self.passport_entry.grid(row=2,column=1)
        self.passport_entry.configure(
            width=20
        )
        self.passport_entry.bind("<FocusOut>", self.__passport_callback)

    def __passport_callback(self, event):
        if(len(self.passport_entry.get()) >= 9):
            self.passport_check_label.configure(bg="#33cc33")
        else:
            self.passport_check_label.configure(bg="#ff0000")


    def __add_passport_check_label(self):
        self.passport_check_label = Label()
        self.passport_check_label.grid(row=2,column=2)
        self.passport_check_label.configure(
            width=2,
            height=1,
            bd=4,
            bg="#ccc"
        )
    
    def __add_nights_label(self):
        self.nights_label = Label()
        self.nights_label.grid(row=3,column=0)
        self.nights_label.configure(
            text="Number of Nights"
        )

    def __add_nights_entry(self):
        self.nights_entry = Entry()
        self.nights_entry.grid(row=3,column=1)
        self.nights_entry.configure(
            width=20
        )
        self.nights_entry.bind("<FocusOut>", self.__nights_callback)

    def __nights_callback(self, event):
        if( int(self.nights_entry.get()) > 0 and int(self.nights_entry.get()) <= 365):
            self.nights_check_label.configure(bg="#33cc33")
        else:
            self.nights_check_label.configure(bg="#ff0000")

    def __add_nights_check_label(self):
        self.nights_check_label = Label()
        self.nights_check_label.grid(row=3,column=2)
        self.nights_check_label.configure(
            width=2,
            height=1,
            bd=4,
            bg="#ccc"
        )

    def __add_checkin_button(self):
        self.checkin_button = Button()
        self.checkin_button.grid(row=4, columnspan=3)
        self.checkin_button.configure(
            text="Check-In"
        )

# Create an object of the Gui class when this module is executed
# This is for convenience. Normally the following would be in the main.py file.
# The if statement simply makes sure that the window is displayed when this file is run
# directly as opposed to being imported into another class.
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()	