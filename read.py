import openpyxl
# read_week(file_path)
# read_days(file_path)
# read_exercises(file_path)
# week = 2D array of every value in excel file
# rozdelenie tyzdnov bude podla toho, ze mam v riadku len jednu bunku, ktora ma v sebe napr. 2. Týždeň- 10.1.2022-16.1.2022 (87,3kg)    - obcas bez zaznamenavanie hmotnosti
# rozdelenie treningov bude podla toho, ze mam prazdny tlpec medzi tabulkami



# nacitanie suboru - budem musiet postupne nacitavat sheety podla toho ci su rozdelene po rokoch alebo po mesiacoch

# workbook = openpyxl.load_workbook(file_path)
# sheet = workbook.active

# max_col = sheet.max_column
# max_row = sheet.max_row