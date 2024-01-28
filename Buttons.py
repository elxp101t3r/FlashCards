from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
import pandas as pd


data = pd.read_csv('./data/se_wordlist.csv')
learn = data.to_dict(orient='records')
print(learn)


def next_card():
    pass
    
  
    

class UnknownBtn:
    def __init__(self):
        self.unknown_btn = Button(text='Unknown', bootstyle='danger-outline', command=next_card)
        self.unknown_btn.grid(column=0, row=2, pady=20)
        
        
class KnownBtn:
    def __init__(self):
        self.known_btn = Button(text='Known', bootstyle='success-outline', command=next_card)
        self.known_btn.grid(column=1, row=2, pady=20)
