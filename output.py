from openpyxl import load_workbook

def main_function(names_of_exercises, all_exercises_dictionary, name_of_day):
    
    path = 'plan.xlsx'
    wb = load_workbook(path)
    sheet = wb.active

    sheet.insert_rows(1, 5)     # pridanie 5 riadkov na zaciatok excelu

    abc = 'BCDEFGHIJKLMNOPQRSTUVWXYZ'


    sheet["A1"] = name_of_day
    sheet['A2'] = 'reps'
    sheet['A3'] = 'kg'

    
    names = []

    for name in names_of_exercises:

        if name != None:
            names.append(name)

    i = 0

    for name in names:
        sheet[abc[i] + '1'] = name
        i += 1
    
    n = 0

    for name in names:
        
        data = all_exercises_dictionary[name][-1]
        
        sheet[abc[n]+'2'] = data[0]
        sheet[abc[n]+'3'] = data[1]
        n += 1

    wb.save(path)
