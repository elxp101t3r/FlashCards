from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from Buttons import KnownBtn, UnknownBtn
from Canvas import CardCanvas

class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()
        self.title('Flashy')
        self.geometry('670x550')
        self.cards = CardCanvas()
        self.known_button = KnownBtn()
        self.unknown_button = UnknownBtn()
        self.mainloop()
