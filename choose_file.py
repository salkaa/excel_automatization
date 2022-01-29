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

    changed_files = list_of_files.copy()

    x = 0

    for file in changed_files:
        index = 0
        for i in range(len(file)):
            if file[i] == '/':
                index = i
        changed_files[x] = file[index+1:]
        x += 1

    file_root = Tk()
    file_root.geometry("800x800")
    file_root.title('vyber excel súbor')
    file_root.resizable(False, False)

    buttons = []

    index = 0

    for file in list_of_files:
        buttons.append(Button(file_root, text=changed_files[index], command=lambda c=file: [change_path(c), file_root.destroy()]))
        buttons[-1].place(width=500, height=30, x=150, y=30+(index*35))
        index += 1
    
    file_root.mainloop()
    return path

