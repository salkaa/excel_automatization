import os, glob
from tkinter import *
from tkinter.ttk import *

path = ''

def change_path(file):
    global path
    path = file


def main():
    global path
    
    dir_name = '/home/salka/Documents/excel_files/'

    # Get list of all files in a given directory sorted by name

    list_of_files = sorted(filter( os.path.isfile, glob.glob(dir_name + '*') ) )
    for file in list_of_files:
        if '.xlsx' not in file:
            list_of_files.remove(file)

    file_root = Tk()
    file_root.geometry("400x400")
    file_root.title('vyber excel súbor')
    file_root.resizable(False, False)

    buttons = []

    index = 0

    for file in list_of_files:
        buttons.append(Button(file_root, text=file, command=lambda c=file: [change_path(c), file_root.destroy()]))
        buttons[-1].place(width=300, x=50, y=30+(index*50))
    
    file_root.mainloop()
    return path

