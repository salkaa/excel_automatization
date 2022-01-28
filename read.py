import openpyxl
path = 'plan.xlsx'

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

max_col = sheet.max_column
max_row = sheet.max_row

# week bude 2d list v ktorom bude nacitany cely excel, s ktorym budem potom pracovat

def read_week():

    week = [] 
    for n in range(1, max_row + 1):

        cellsrow = []

        for i in range (1, max_col):

            bunka = sheet.cell(row = n, column = i)
            cellsrow.append(bunka.value)

        if cellsrow[0] != None:
            week.append(cellsrow)

    return week

# dictionary treningov PULL+LEGS, PUSH+LEGS, PULL, LEGS, PUSH, values nazvy vsetkych cvikov pre ten trening

def read_days(week=read_week()):

    days = {}

    for i in range(len(week)//3):

        if week[i*3][0] not in days:
            days[week[i*3][0]] = list(week[i*3][n] for n in range(1, len(week[i*3])))

            while None in days[week[i*3][0]]:
                    days[week[i*3][0]].remove(None)
                    

        else: pass
    
    return days

# dictionary vsetkych cvikov, key nazov cviku, value 2d list s [reps, weights]

def read_exercises(week=read_week()):

    exercises = {}
    counter = 0
    for row in week:

        week[counter] = row[1:]
        counter += 1

    for i in range(len(week)//3):

        index = 0
        for element in week[i*3]:

            if element not in exercises:    
                exercises[element] = [[week[i*3 + 1][index], week[i*3 + 2][index]]]
            else:
                exercises[element].append([week[i*3 + 1][index], week[i*3 + 2][index]])
            index += 1
    
    return exercises