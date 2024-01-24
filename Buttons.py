from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *


class NextBtn:
    def __init__(self):
        self.next_btn = Button(text='Next', bootstyle='outline')
        self.next_btn.grid(column=0, row=2, pady=20)
        
        
class PreviousBtn:
    def __init__(self):
        self.previous_btn = Button(text='Previous', bootstyle='Danger-outline')
        self.previous_btn.grid(column=1, row=2, pady=20)
