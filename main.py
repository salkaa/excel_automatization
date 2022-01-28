from tkinter import *
from tkinter.ttk import *
import read, output, openpyxl

days = read.read_days()
week = read.read_week()
exercises = read.read_exercises()


#----------------------------------------------------------------------------------------------------------#
# pracovanie s nacitanymi datami z excelu v kinteri a front end tkinteru


class Display:

    # inicializacia tkinteru a spustenie hlavnych funkcii classy
    def __init__(self, days, exercises):

        self.root = Tk()
        self.root.geometry("620x620") # maximum 5x5 buttonov
        self.root.title('vyber tréning, ktorý chceš vytvoriť')
        self.root.resizable(False, False)
        
        self.days = days # dictionary treningov so vsetkymi nazmi cvikov v tom treningu
        self.exercises = exercises # dictionary vsetkych cvikov s kg a reps
        self.index = 0
        self.button_names = list(self.days.keys())

        self.create_buttons()
        self.create_button_new_exercise()
        
    # vytvori vsetky buttons, ktore budu dnami uz napisane v exceli
    def create_buttons(self):

        name = 'button'
        for i in range(len(self.button_names)):

            this_button = self.button_names[i]
            globals()[name + str(i)] = Button(self.root, text=this_button)
            globals()[name + str(i)]["command"] = lambda c=i: self.new_display(c)

            a = self.index//5
            b = self.index%5

            globals()[name + str(i)].place(width=100, height=100, x=b*100+20*(b+1), y=a*100+20*(a+1))
            self.index += 1

    # vytvori button + na vytvorenie noveho dna
    def create_button_new_exercise(self):

        s = Style()
        s.configure('my.TButton', font=('Helvetica', 30))

        a = self.index//5
        b = self.index%5
        bx, by = b*100+20*(b+1), a*100+20*(a+1)

        self.creator_button = Button(self.root, text='+', style='my.TButton', command=lambda: [self.entry_new_training(), self.create_or_cancel()])
        self.creator_button.place(width=100, height=100, x=bx, y=by)

    # vytvori entry, ktore sa pusti po stlaceni create_button_new_exercise()
    def entry_new_training(self):

        self.training_entry = Entry(self.root)
        
        a = self.index//5
        b = self.index%5
        bx, by = b*100+20*(b+1)+5, a*100+20*(a+1)+40

        self.training_entry.place(width=90, x=bx, y=by)

        self.entry_label = Label(self.root, text='Zadaj názov:')
        self.entry_label.place(x=bx+5, y=(by-20))
    
    # vytvori buttony pre entry, aby sa dalo zatvorit alebo zapisat zadany nazov dna
    def create_or_cancel(self):

        a = self.index//5
        b = self.index%5
        bx, by = b*100+20*(b+1)+15, a*100+20*(a+1)+65

        self.ok_button = Button(self.root, text='Ok', command=self.create_new_training)
        self.ok_button.place(width=30, height=30, x=bx, y=by)

        self.cancel_button = Button(self.root, text='X', command=self.cancel)
        self.cancel_button.place(width=30, height=30, x=bx+40, y=by)

    # stlacenie X buttonu pri entry
    def cancel(self):

        self.cancel_button.destroy()
        self.ok_button.destroy()
        self.training_entry.destroy()
        self.entry_label.destroy()

    # stlacenie Ok buttonu pri entry
    def create_new_training(self):
         
        new_name = self.training_entry.get().upper()
        self.days[new_name] = []
        self.button_names.append(new_name)
        self.cancel()

        a = self.index//5
        b = self.index%5
        bx, by = b*100+20*(b+1), a*100+20*(a+1)


        globals()['button' + str(self.index)] = Button(self.root, text=new_name, command=lambda c=self.index : self.new_display(c))
        globals()['button' + str(self.index)].place(width=100, height=100, x=bx, y=by)

        self.creator_button.destroy()
        self.index += 1
        self.create_button_new_exercise()

    # novy tkinter po stlaceni lubovolneho buttonu
    def new_display(self, num):

        self.ex = self.days[self.button_names[num]]
        self.new_root = Tk()
        self.new_root.geometry('800x800')
        self.new_root.title(self.button_names[num])
        self.new_root.resizable(False, False)

        self.lines = []

        self.coor = [20, 55]

        self.label_name = Label(self.new_root, text='name')
        self.label_name.place(x=20, y=10)

        self.label_reps = Label(self.new_root, text='reps')
        self.label_reps.place(x=320, y=10)

        self.label_kg = Label(self.new_root, text='kg')
        self.label_kg.place(x=394, y=10)

        self.first_separator = Separator(self.new_root, orient='horizontal')
        self.first_separator.place(width=800, y=37)

        self.second_separator = Separator(self.new_root, orient='vertical')
        self.second_separator.place(height=800, x=self.coor[0]+355)

        self.export_button = Button(self.new_root, text='UPLOAD TO EXCEL', command=lambda : self.export_data(num))
        self.export_button.place(width=150, height=50, x=515, y=735)

        self.ii = 0

        for exercise in self.ex:
            globals()[exercise + 'label'] = Label(self.new_root, text=exercise)
            globals()[exercise + 'label'].place(x=self.coor[0], y=self.coor[1])
            
            reps = self.exercises[exercise][-1][0]
            kg = int(self.exercises[exercise][-1][1])

            globals()[exercise + 'lastreps'] = Entry(self.new_root)
            globals()[exercise + 'lastreps'].insert(END, str(reps))
            globals()[exercise + 'lastreps'].place(width=60, x=self.coor[0]+270, y=self.coor[1]-1)

            globals()[exercise + 'lastkg'] = Entry(self.new_root)
            globals()[exercise + 'lastkg'].insert(END, str(kg))
            globals()[exercise + 'lastkg'].place(width=60, x=self.coor[0]+374, y=self.coor[1]-1)

            globals()[exercise + 'calcbutton'] = Button(self.new_root, text='+5', command=lambda c=exercise: self.button_calc(c, 5))
            globals()[exercise + 'calcbutton'].place(width=50, x=570, y=self.coor[-1]-5)

            globals()[exercise + 'calcbutton1'] = Button(self.new_root, text='+2.5', command=lambda c=exercise: self.button_calc(c, 2.5))
            globals()[exercise + 'calcbutton1'].place(width=50, x=510, y=self.coor[-1]-5)

            globals()[exercise + 'load'] = Button(self.new_root, text='load', command=lambda c=exercise: self.button_load(c))
            globals()[exercise + 'load'].place(width=50, x=630, y=self.coor[-1]-5)

            globals()[exercise + 'delete'] = Button(self.new_root, text='delete', command=lambda c=exercise: self.button_delete(c))
            globals()[exercise + 'delete'].place(width=70, x=690, y=self.coor[-1]-5)
            
            self.lines.append(Separator(self.new_root, orient='horizontal'))
            self.lines[-1].place(width=800, x=0, y=self.coor[1]+33)
            
            self.ii += 1
            self.coor[1] += 50

        self.value_combobox = StringVar()
        self.option_menu = Combobox(self.new_root, width=26, textvariable=self.value_combobox)
        self.option_menu.place(x=self.coor[0], y=760)

        self.option_menu['values'] = tuple(self.exercises.keys())
        self.option_menu.current(1)

        self.combo_button = Button(self.new_root, text='create', command=lambda : self.add_new_exercise())
        self.combo_button.place(x=self.coor[0]+230, y=757)

    # command na ulozenie entry do dictionary exercises
    def command_button_save(self):

        for exercise in self.ex:

            data = []
            data.append(globals()[exercise + 'lastreps'].get())
            data.append(globals()[exercise + 'lastkg'].get())

            if data != self.exercises[exercise][-1]:
                self.exercises[exercise].append(data)

    # button na pridanie 10% kg k poslednemu cviku
    def button_calc(self, exercise, number):

        kg = globals()[exercise + 'lastkg'].get()
        
        globals()[exercise + 'lastkg'].delete(0, END)

        kg = str(float(kg)+number)

        if kg[-1] == '0':
            kg = kg[:-2]

        globals()[exercise + 'lastkg'].insert(END, str(kg))
    
    # button ktory nacita do entry posledne ulozene kg a reps
    def button_load(self, exercise):
        
        reps = self.exercises[exercise][-1][0]
        kg = self.exercises[exercise][-1][1]

        globals()[exercise + 'lastreps'].delete(0, END)
        globals()[exercise + 'lastkg'].delete(0, END)

        globals()[exercise + 'lastreps'].insert(END, str(reps))
        globals()[exercise + 'lastkg'].insert(END, str(kg))

    # button ktory vymaze cvik z treningu
    def button_delete(self, val):

        globals()[val + 'lastreps'].destroy()
        globals()[val + 'lastkg'].destroy()
        globals()[val + 'calcbutton'].destroy()
        globals()[val + 'calcbutton1'].destroy()
        globals()[val + 'load'].destroy()
        globals()[val + 'delete'].destroy()
        globals()[val + 'label'].destroy()

        x = self.ex.index(val)
        self.ex[x] = None

        for i in range(len(self.lines)):

            if self.ex[i] == None:

                if self.lines[i] != None:

                    x = self.lines[i]
                    x.destroy()
                    self.lines[i] = None


    # button ktory zoberie nazov z comboboxu
    def add_new_exercise(self):

        val = self.option_menu.get()

        if val not in self.exercises.keys():
            self.exercises[val] = [[0, 0]]
            

        if val not in self.ex:
            self.ex.append(val)
            reps = self.exercises[val][-1][0]
            kg = self.exercises[val][-1][1]


            globals()[val + 'label'] = Label(self.new_root, text=val)
            globals()[val + 'label'].place(x=self.coor[0], y=self.coor[1])
            
            reps = self.exercises[val][-1][0]
            kg = int(self.exercises[val][-1][1])

            globals()[val + 'lastreps'] = Entry(self.new_root)
            globals()[val + 'lastreps'].insert(END, str(reps))
            globals()[val + 'lastreps'].place(width=60, x=self.coor[0]+270, y=self.coor[1])

            globals()[val + 'lastkg'] = Entry(self.new_root)
            globals()[val + 'lastkg'].insert(END, str(kg))
            globals()[val + 'lastkg'].place(width=60, x=self.coor[0]+374, y=self.coor[1])

            globals()[val + 'calcbutton'] = Button(self.new_root, text='+5', command=lambda c=val: self.button_calc(c, 5))
            globals()[val + 'calcbutton'].place(width=50, x=570, y=self.coor[-1]-5)

            globals()[val + 'calcbutton1'] = Button(self.new_root, text='+2.5', command=lambda c=val: self.button_calc(c, 2.5))
            globals()[val + 'calcbutton1'].place(width=50, x=510, y=self.coor[-1]-5)

            globals()[val + 'load'] = Button(self.new_root, text='load', command=lambda c=val: self.button_load(c))
            globals()[val + 'load'].place(width=50, x=630, y=self.coor[-1]-5)

            globals()[val + 'delete'] = Button(self.new_root, text='delete', command=lambda c=val: self.button_delete(c))
            globals()[val + 'delete'].place(width=70, x=690, y=self.coor[-1]-5)
                
            self.lines.append(Separator(self.new_root, orient='horizontal'))
            self.lines[-1].place(width=800, x=0, y=self.coor[1]+33)

            self.ii += 1
            self.coor[1] += 50
    
    # funkcia ktora vymaze tkinter treningu a uploadne data do excelu pomocou suboru output
    def export_data(self, training_index):

        self.command_button_save()
        output.main_function(self.ex, self.exercises, self.button_names[training_index])
        self.new_root.destroy()


# spustenie hlavnej classy
x = Display(days, exercises)

x.root.mainloop()
x.new_root.mainloop()

