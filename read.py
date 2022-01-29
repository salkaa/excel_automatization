import openpyxl

# week = 2D array of every value in excel file

def read_week(file_path):

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    max_col = sheet.max_column
    max_row = sheet.max_row

    week = [] 
    for n in range(1, max_row + 1):

        cellsrow = []

        for i in range (1, max_col):

            bunka = sheet.cell(row = n, column = i)
            cellsrow.append(bunka.value)

        if cellsrow[0] != None:
            week.append(cellsrow)

    return week

# dictionary with keys as names of body parts that will be trained in that session and keys as exercises

def read_days(file_path):

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    max_col = sheet.max_column
    max_row = sheet.max_row

    days = {}

    week = read_week(file_path)

    for i in range(len(week)//3):

        if week[i*3][0] not in days:
            days[week[i*3][0]] = list(week[i*3][n] for n in range(1, len(week[i*3])))

            while None in days[week[i*3][0]]:
                    days[week[i*3][0]].remove(None)
                    

        else: pass
    
    return days

# dictionary of all exercises in excel file with values as array [[reps1, kg1], [reps2, kg2]]

def read_exercises(file_path):

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    max_col = sheet.max_column
    max_row = sheet.max_row

    week = read_week(file_path)

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