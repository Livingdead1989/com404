from tkinter import *

#colours
grey = "#eee"

# list of object parameters will not run on its own

class Gui(Tk):
    # init constructor
    def __init__(self):
        # super pulls from the parent
        super().__init__()

        # set window attributes
        #self.geometry("400x180")
        self.title("Newsletter")

        # add window components by
        self.__add_outer_frame()
        self.__add_containter_frame()
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_subscribe_button()

        # style component
        self.configure(
        )
    
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(
            bd = 10,
            bg = "#474747"
        )

    def __add_containter_frame(self):
        self.containter_frame = Frame(self.outer_frame)
        self.containter_frame.grid(row=0, column=0)
        self.containter_frame.configure(
            bg = grey

        )

    # two underscores makes it a private function
    def  __add_heading_label(self):

        # pass doesn't do anything its a placeholder that allows the code to run without anything
        # pass

        # create component
        self.heading_label = Label(self.containter_frame)
        self.heading_label.grid(row=0, column=0)
        # style component
        self.heading_label.configure(
            font = "Arial 24", 
            text = "RECEIVE OUR NEWSLETTER",
            pady = 10,
            bg = grey
            )
        # handle events for component

    def  __add_message_label(self):

        # pass doesn't do anything its a placeholder that allows the code to run without anything
        # pass

        # create component
        self.message_label = Label(self.containter_frame)
        self.message_label.grid(row=1, column=0)
        # style component
        self.message_label.configure(
            font = "Arial 16",
            text = "Please enter your email below to receive our newletter",
            pady = 10,
            bg = grey
            )
        # handle events for component

    def __add_email_frame(self):
        self.email_frame = Frame(self.containter_frame)
        self.email_frame.grid(row=2, column=0, columnspan=2)
        self.email_frame.configure(
            pady = 10,
            bg = grey
        )

    def __add_email_label(self):
        # create component
        self.email_label = Label(self.email_frame)
        self.email_label.grid(row=0, column=0)
        # style component
        self.email_label.configure(
            font = "Arial 14",
            text = "Email:",
            bg = grey
        )

    def __add_email_entry(self):
        # create component
        self.email_entry = Entry(self.email_frame)
        self.email_entry.grid(row=0, column=1)
        # style component
        self.email_entry.configure(
            font = "Arial 14"
        )

    def __add_subscribe_button(self):
        # create component
        self.subscribe_button = Button(self.containter_frame)
        self.subscribe_button.grid(row=3, column=0)
        # style component
        self.subscribe_button.configure(
            font = "Arial 16",
            text = "Subscribe",
            bg = "#f00",
            #macOS requirement
            highlightbackground="#f00"
            
        )

    # handle events
    # (callback functions to handle events will go here)