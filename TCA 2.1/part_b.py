from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # Load Resources
        self.default_image = PhotoImage(file="default.gif")
        self.filled_image = PhotoImage(file="filled.gif")
        self.empty_image = PhotoImage(file="empty.gif")

        # Options Menu
        self.options = StringVar()
        self.options.set("Weekly")

        self.title("Newsletter")
        self.__add_container_frame()
        self.__add_window_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_email_image_label()
        self.__add_type_frame()
        self.__add_type_label()
        self.__add_type_optionmenu()
        self.__add_subscribe_button()
    
    def __add_container_frame(self):
        self.container_frame = Frame()
        self.container_frame.pack()
        self.container_frame.configure(
            bg = "#ddd",
            padx = 10,
            pady = 10
        )

    def __add_window_frame(self):
        self.window_frame = Frame(self.container_frame)
        self.window_frame.pack()
        self.window_frame.configure(
            bg = "#eee",
            # padx = 10,
            # pady = 10
        )

    def __add_heading_label(self):
        # Create
        self.heading_label = Label(self.window_frame)
        # Place
        self.heading_label.grid(row=0)
        # Configure
        self.heading_label.configure(
            text = "RECEIVE OUR NEWSLETTER",
            font = "Arial 14",
            pady = 10
        )
    def __add_instruction_label(self):
        # Create
        self.instruction_label = Label(self.window_frame)
        # Place
        self.instruction_label.grid(row=1, sticky=W)
        # Configure
        self.instruction_label.configure(
            text = "Please enter your email below to receive our newsletter.",
            pady = 10,
            padx = 10
        )
    def __add_email_frame(self):
        # Create
        self.email_frame = Frame(self.window_frame)
        # Place
        self.email_frame.grid(row=2, sticky=W)
        self.email_frame.configure(
            padx = 10
        )

    def __add_email_label(self):
        # Create
        self.email_label = Label(self.email_frame)
        # Place
        self.email_label.grid(row=0, column=0)
        # Configure
        self.email_label.configure(
            text="Email:",
            padx = 10,
            pady = 10
        )

    def __add_email_entry(self):
        # Create
        self.email_entry = Entry(self.email_frame)
        # Place
        self.email_entry.grid(row=0, column=1)
        # Configure
        self.email_entry.configure(
            width = 30,
            bd = 2,
            fg = "#f00"
        )
        # Bind
        self.email_entry.bind("<KeyRelease>", self.__email_callback)

    # event handler for image change
    def __email_callback(self, event):
        if(len(self.email_entry.get()) >= 1):
            self.email_image_label.configure(image= self.filled_image)
        else:
            self.email_image_label.configure(image= self.empty_image)
            

    def __add_email_image_label(self):
        self.email_image_label = Label(self.email_frame)
        self.email_image_label.grid(row=0, column=3)
        self.email_image_label.configure(
            image = self.default_image,
            height = 16,
            width = 16
        )


    def __add_type_frame(self):
        # Create
        self.type_frame = Frame(self.window_frame)
        # Place
        self.type_frame.grid(row=3, sticky=W)
        self.type_frame.configure(
            padx = 10
        )

    def __add_type_label(self):
        # Create
        self.type_label = Label(self.type_frame)
        # Place
        self.type_label.grid(row=0, column=0)
        # Configure
        self.type_label.configure(
            text="Type",
            padx = 10,
            pady = 10
        )

    def __add_type_optionmenu(self):
        self.type_optionmenu = OptionMenu(self.type_frame, self.options, "Weekly", "Monthly", "Yearly")
        self.type_optionmenu.grid(row=0, column=1)
        self.type_optionmenu.configure(
        )

    def __add_subscribe_button(self):
        # Create
        self.subscribe_button = Button(self.container_frame)
        # Place
        self.subscribe_button.pack(fill=X)
        # Configure
        self.subscribe_button.configure(
            text = "Subscribe",
            bg = "#fee"
        )
        # Binds the event ButtonRelease-1 (left mouse) to an event called buy_button_clicked
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)
    
    # event handler for messagebox
    def __subscribe_button_clicked(self, event):
        if(len(self.email_entry.get()) >= 1):
            # read from the options menu to provide answers based on what has been set
            if(self.options.get() == "Weekly"):
                messagebox.showinfo("Newletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
            elif(self.options.get() == "Monthly"):
                messagebox.showinfo("Newletter", "You have subscribed to the monthly newsletter! You will receive this on the first day of each month.")
            elif(self.options.get() == "Yearly"):
                messagebox.showinfo("Newletter", "You have subscribed to the yearly newsletter! You will receive this at the start of each year.")
            else:
                messagebox.showinfo("Newletter", "Error, please try again.")
        else:
            messagebox.showinfo("Newletter", "Please enter your email!")



# the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop() 