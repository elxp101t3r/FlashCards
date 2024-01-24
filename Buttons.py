from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *


class NextBtn:
    def __init__(self):
        self.next_btn = Button(text='Next', bootstyle='Danger')
        self.next_btn.grid(column=0, row=2)
        
        
class PreviousBtn:
    def __init__(self):
        self.previous_btn = Button(text='Previous', bootstyle='Success')
        self.previous_btn.grid(column=2, row=2)
