from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Tickets")

        self.__add_heading_label()
        self.__add_lyric_frame()
        self.__add_lyric_label()
        self.__add_lyric_entry()
        self.__add_add_button()
        self.__add_lyrics_label()
        self.__add_lyrics_listbox()

    def __add_heading_label(self):
        # Create
        self.heading_label = Label()
        # Place
        self.heading_label.grid(row=0, column=0)
        # Style
        self.heading_label.configure(
            text = "Song Maker",
            font = "Arial 18"
        )
        # Event

    def __add_lyric_frame(self):
        # Create
        # Place
        # Style
        # Event
        pass

    def __add_lyric_label(self):
        # Create
        # Place
        # Style
        # Event
        pass

    def __add_lyric_entry(self):
        # Create
        # Place
        # Style
        # Event
        pass

    def __add_add_button(self):
        # Create
        # Place
        # Style
        # Event
        pass

    def __add_lyrics_label(self):
            # Create
            # Place
            # Style
            # Event
            pass

    def __add_lyrics_listbox(self):
        # Create
        # Place
        # Style
        # Event
        pass

        
    