from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *


class CardCanvas:
    def __init__(self):
        self.cnv = Canvas(width=600, height=400, bg='white')
        self.cnv.grid(column=0, row=0, columnspan=2, padx=35)
        self.cnv.create_rectangle((100, 100), (500, 500), fill='#d6b37e')
        self.cnv.create_text(
            (300, 200),
            text="Front:",
            font=(('Arial', 18, 'italic')),
            fill='black'
        )
        self.cnv.create_text(
            (300, 250),
            text="Q1",
            font=("Arial", 20, "bold"),
            fill='black'
        )
