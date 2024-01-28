from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
import pandas as pd
from random import choice


data = pd.read_csv('./data/se_wordlist.csv')
learn = data.to_dict(orient='records')


class Win(Tk):
    def __init__(self):
        super().__init__()
        self.title('Flashy')
        self.geometry('670x550')
        self.cnv = Canvas(width=600, height=400, bg='white')
        self.cnv.grid(column=0, row=0, columnspan=2, padx=35)
        self.cnv.create_rectangle((100, 100), (500, 500), fill='#d6b37e')
        self.card_title = self.cnv.create_text(
            (300, 200),
            text="Front:",
            font=(('Arial', 18, 'italic')),
            fill='black'
        )
        self.card_word = self.cnv.create_text(
            (300, 250),
            text="Q1",
            font=("Arial", 20, "bold"),
            fill='black'
        )
        self.known_btn = Button(text='Known', bootstyle='warning-outline', command=self.next_card)
        self.known_btn.grid(column=1, row=2, pady=20)
        self.unknown_btn = Button(text='Unknown', bootstyle='primary-outline', command=self.next_card)
        self.unknown_btn.grid(column=0, row=2, pady=20)
        self.mainloop()
        
        
    def next_card(self):
        self.current_card = choice(learn)
        self.cnv.itemconfig(self.card_title, text='Sweedish')
        self.cnv.itemconfig(self.card_word, text=self.current_card['Sweedish'])
