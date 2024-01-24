from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from Buttons import NextBtn, PreviousBtn
from Canvas import CardCanvas

class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()
        self.title('Flashy')
        self.geometry('670x550')
        self.cards = CardCanvas()
        self.next = NextBtn()
        self.previous = PreviousBtn()
        self.mainloop()
