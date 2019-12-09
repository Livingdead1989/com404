from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # Load Resources
        self.default_image = PhotoImage(file="default.gif")
        self.filled_image = PhotoImage(file="filled.gif")
        self.empty_image = PhotoImage(file="empty.gif")
        self.weekly_image = PhotoImage(file="weekly.gif")
        self.monthly_image = PhotoImage(file="monthly.gif")
        self.yearly_image = PhotoImage(file="yearly.gif")

        # Options Menu
        self.options = StringVar()
        self.options.set("Weekly")

        # Animation Button State
        self.button_state = "stopped"
        self.animation_x_pos = 0
        self.animation_y_pos = 100 - 32
        self.animation_x_change = 1
        self.animation_y_change = 1

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
        self.__add_animation_button()
        self.__add_animation_window_frame()
        self.__add_animation_image_label()

        # start the timer
        self.tick()
    
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
            width = 30,
            bd = 2
        )


    # SUBSCRIBE BUTTON
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



    # ANIMATION BUTTON
    def __add_animation_button(self):
        # Create
        self.animation_button = Button(self.container_frame)
        # Place
        self.animation_button.pack(fill=X)
        # Configure
        self.animation_button.configure(
            text = "Start Animation",
            bg = "#fee"
        )
         # Binds the event ButtonRelease-1 (left mouse) to an event
        self.animation_button.bind("<ButtonRelease-1>", self.__animation_button_clicked)
        

    # event handler
    def __animation_button_clicked(self, event):
        if(self.button_state == "stopped"):
            self.button_state = "running"
            self.animation_button.configure(text="Stop Animation")

            if(self.options == "Weekly"):        
                self.animation_image_label.configure(image=self.weekly_image)
            elif(self.options == "Monthly"):
                self.animation_image_label.configure(image=self.monthly_image)
            elif(self.options == "Yearly"):
                self.animation_image_label.configure(image=self.yearly_image)
        else:
            self.animation_button.configure(text="Start Animation")
            self.button_state = "stopped"


    # Animation Window

    def __add_animation_window_frame(self):
        self.animation_window_frame = Frame(self.container_frame)
        self.animation_window_frame.pack(fill=X)
        self.animation_window_frame.configure(
            height = 200,
            bg = "#aac9b3"
        )

    # the timer tick function    
    def tick(self):
        # Animation
        if(self.animation_x_pos >= 320 - 64):
            # Hit the right side of the container window
            self.animation_x_change = -1

        elif(self.animation_x_pos <= 0):
            # Hit the left side of the container window
            self.animation_x_change = 1

        elif(self.animation_y_pos >= 200 - 64):
            # Hit the bottom side of the container window
            self.animation_y_change = -1

        elif(self.animation_y_pos <= 0):
            # Hit the top side of the container window
            self.animation_y_change = 1
        
        # THE MOVEMENT
        if(self.button_state == "running"):
            self.animation_x_pos = self.animation_x_pos + self.animation_x_change
            self.animation_y_pos = self.animation_y_pos + self.animation_y_change
            self.animation_image_label.place(
                x=self.animation_x_pos,
                y=self.animation_y_pos
            )
        #THE TICK
        self.after(25, self.tick)
    
    # the animation image
    def __add_animation_image_label(self):
        self.animation_image_label = Label(self.animation_window_frame)
        self.animation_image_label.place(
            x=self.animation_x_pos,
            y=self.animation_y_pos
        )
        self.animation_image_label.configure(image=self.weekly_image)


# the object
if __name__ == "__main__":
    gui = Gui()    
    gui.mainloop() 