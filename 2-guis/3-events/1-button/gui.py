from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tickets")

        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
    
    def __add_heading_label(self):
        # Create
        self.heading_label = Label()
        # Place
        self.heading_label.grid(row=0, column=0)
        # Configure
        self.heading_label.configure(
            text = "Entrance Ticket",
            font = "Arial 18"
        )
    def __add_instruction_label(self):
        # Create
        self.instruction_label = Label()
        # Place
        self.instruction_label.grid(row=1, column=0, sticky=W)
        # Configure
        self.instruction_label.configure(
            text = "How many tickets are needed?"
        )

    def __add_tickets_entry(self):
        # Create
        self.tickets_entry = Entry()
        # Place
        self.tickets_entry.grid(row=2, column=0)
        # Configure
        self.tickets_entry.configure(
            width=3
        )

    def __add_buy_button(self):
        # Create
        self.buy_button = Button()
        # Place
        self.buy_button.grid(
            row=3, 
            column=0,
            pady=5
        )
        # Configure
        self.buy_button.configure(
            text = "BUY",
            padx = 10,
            pady = 5
        )
        # Bind
        # Binds the event ButtonRelease-1 (left mouse) to an event called buy_button_clicked
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)
    
    # event handler
    def __buy_button_clicked(self, event):
        if(int(self.tickets_entry.get()) == 1):
            messagebox.showinfo("Purchased a Ticket!", "You have purchased a ticket.")
        elif(int(self.tickets_entry.get()) >= 2):
            messagebox.showinfo("Purchased Tickets!", "You have purchased " + self.tickets_entry.get() + " tickets.")  
        else:
            messagebox.showinfo("Error!", "You have entered an invalid number of tickets.")

