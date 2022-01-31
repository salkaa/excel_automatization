import openpyxl

# read_data(file_path) - 2d list vsetkych dat v exceli
# read_days(file_path) - dictionary s nazvami treningov ako keys a cvikmi ako values
# read_exercises(file_path)
# read.read_tyzden(file_path)
# read.read_sheet_sorted_by_date(file_path)
# week = 2D array of every value in excel file
# rozdelenie tyzdnov bude podla toho, ze mam v riadku len jednu bunku, ktora ma v sebe napr. 2. Týždeň- 10.1.2022-16.1.2022 (87,3kg)    - obcas bez zaznamenavanie hmotnosti
# rozdelenie treningov bude podla toho, ze mam prazdny tlpec medzi tabulkami
# pri kazdom cviku bude aj komentar o tom aky bol - moze byt prazdny - ak je prazdny tak tam chcecm napisat no comment
# kazdy cvik bude mat urcenu aj nejaku farbu, ktoru si chcem pamatat

# nacitanie suboru - budem musiet postupne nacitavat sheety podla toho ci su rozdelene po rokoch alebo po mesiacoch

def read_data(file_path):

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    max_col = sheet.max_column
    max_row = sheet.max_row
    data = [max_row*[]]

    for i in range(2, max_row + 1):
        for n in range(1, max_col + 1):
            data[i].append(sheet.cell(row = i, column = n))

    # podla tyzdnov to viem teraz rozdelit podla toho kde je list len s jednou value a ostatne su none

    week_headers = [] # 2d list s value a indexom row v ktorom tento header je
    week = []         # 2d list 
    
    for i in range(len(data)):
        
        checker = True

        for n in range(1, len(data[i])):
            if data[i][n] != None:
                checker = False

        if checker == True:

            if len(week_headers) >= 1:
                week.append(data[week_headers[-1][1]+1:i])
            else:
                week.append(data[:i])

            week_headers.append([data[i][0], i])
            
    # teraz potrebujem kazdy list v tomto liste rozdelit na tretiny podla toho kde je medzera