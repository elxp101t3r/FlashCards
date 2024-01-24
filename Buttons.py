from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *


class Btn(Button):
    def __init__(self):
        super().__init__()


class NextBtn(Btn):
    def __init__(self):
        super().__init__()
        self.next_btn = Button(text='Next', bootstyle='Danger')
        self.next_btn.grid(column=0, row=0)
        
        
class PreviousBtn(Btn):
    def __init__(self):
        super().__init__()
        self.previous_btn = Button(text='Previous', bootstyle='Success')
        self.previous_btn.grid(column=1, row=0)
        