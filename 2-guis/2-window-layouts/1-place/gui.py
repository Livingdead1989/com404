from tkinter import *

bg_color = "#ccc"

# list of object parameters will not run on its own

class Gui(Tk):
    # init constructor
    def __init__(self):
        # super pulls from the parent
        super().__init__()

        # set window attributes
        self.geometry("400x180")
        self.title("Newsletter")

        # add window components by
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

        # style component
        self.configure(
            bg = bg_color,
            bd = 5
        )

    # two underscores makes it a private function
    def  __add_heading_label(self):

        # pass doesn't do anything its a placeholder that allows the code to run without anything
        # pass

        # create component
        self.heading_label = Label()
        self.heading_label.place(x=15, y=0)
        # style component
        self.heading_label.configure(
            font = "Arial 24", 
            text = "RECEIVE OUR NEWSLETTER",
            bg = bg_color
            )
        # handle events for component

    def  __add_message_label(self):

        # pass doesn't do anything its a placeholder that allows the code to run without anything
        # pass

        # create component
        self.message_label = Label()
        self.message_label.place(x=10, y=40)
        # style component
        self.message_label.configure(
            font = "Arial 16",
            bg = bg_color,
            text = "Please enter your email below to receive our newletter"
            )
        # handle events for component

    def __add_email_label(self):
        # create component
        self.email_label = Label()
        self.email_label.place(x=5, y=80)
        # style component
        self.email_label.configure(
            font = "Arial 14",
            text = "Email:",
            bg = bg_color
        )

    def __add_email_entry(self):
        # create component
        self.email_entry = Entry()
        self.email_entry.place(x=58, y=75)
        # style component
        self.email_entry.configure(
            font = "Arial 14",
            width = "39"
        )

    def __add_subscribe_button(self):
        # create component
        self.subscribe_button = Button()
        self.subscribe_button.place(x=5, y=120)
        # style component
        self.subscribe_button.configure(
            font = "Arial 16",
            text = "Subscribe",
            padx = "10",
            pady = "10",
            bg = "#f00",
            #macOS requirement
            highlightbackground="#f00",
            width = "40"
        )

    # handle events
    # (callback functions to handle events will go here)