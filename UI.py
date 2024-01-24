from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from Buttons import NextBtn, PreviousBtn

class Win(Tk):
    def __init__(self):
        super(Win, self).__init__()
        self.title('Flashy')
        self.geometry('800x526')
        self.next = NextBtn()
        self.previous = PreviousBtn()
        self.mainloop()
