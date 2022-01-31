from tkinter import *
from tkcalendar import Calendar
import datetime

datum = ''

def get_date(chosen_date):

    global datum
    datum = chosen_date

def display():

    global datum
    
    today = str(datetime.date.today())

    root = Tk()
    root.geometry("600x600")
    
    cal = Calendar(root, selectmode = 'day', year = int(today[:4]), month = int(today[5:7]), day = int(today[8:]))
    
    cal.place(width=500, height=500, x=50, y=50)
    
    Button(root, text = "Get Date",
        command = lambda:[get_date(cal.get_date()), root.destroy()]).pack(pady = 18)
    
    root.mainloop()
    return datum