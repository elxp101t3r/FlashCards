from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
import pandas as pd
from random import choice


data = pd.read_csv('./data/se_wordlist.csv')
learn = data.to_dict(orient='records')
current_card = {}


class Win(Tk):
    def __init__(self):
        super().__init__()
        self.title('Flashy')
        self.geometry('670x550')
        self.cnv = Canvas(width=600, height=400, bg='white')
        self.cnv.grid(column=0, row=0, columnspan=2, padx=35)
        self.front = self.cnv.create_rectangle((100, 100), (500, 500), fill='green')
        self.card_title = self.cnv.create_text(
            (300, 200),
            text="",
            font=(('Arial', 18, 'italic')),
            fill='white'
        )
        self.card_word = self.cnv.create_text(
            (300, 250),
            text="",
            font=("Arial", 20, "bold"),
            fill='white'
        )
        self.known_btn = Button(text='Known', bootstyle='success-outline', command=self.next_card)
        self.known_btn.grid(column=1, row=2, pady=20)
        self.unknown_btn = Button(text='Unknown', bootstyle='danger-outline', command=self.next_card)
        self.unknown_btn.grid(column=0, row=2, pady=20)
        self.after(3000, func=self.flip)
        self.next_card()
        self.mainloop()
        
        
    def next_card(self):
        global current_card
        current_card = choice(learn)
        self.cnv.itemconfig(self.card_title, text='Sweedish')
        self.cnv.itemconfig(self.card_word, text=current_card['Sweedish'])
    
    def flip(self):
        global current_card
        self.cnv.itemconfig(self.card_title, text='English', fill='black')
        self.cnv.itemconfig(self.card_word, text=current_card['English'], fill='black')
        self.cnv.itemconfig(self.front, fill='#d4bf37')
        
