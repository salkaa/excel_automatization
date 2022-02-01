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

def read_data():

    workbook = openpyxl.load_workbook('/home/salka/Documents/excel_files/new_plan.xlsx')
    sheet = workbook.active

    max_col = sheet.max_column
    max_row = sheet.max_row

    data = [] # mam 2d list so vsetkymi bunkami, ktore su string

    for i in range(2, max_row+1):
        value_row = []
        for n in range(1, max_col+1):
            x = sheet.cell(row = i, column = n)
            if isinstance(x.value, str):
                value_row.append(x.value)
        data.append(value_row)

    headers_of_weeks = [] # mam 2d list s nazvami tyzdnov a ich indexami v data
    indexes = []
    for value in data:
        if len(value) == 1 and "Týždeň" in value[0]:
            indexes.append(data.index(value))
            headers_of_weeks.append([value, data.index(value)])
    
    print('\nheaders of weeks:\n\n', headers_of_weeks)
    
    weeks_dict = {} # data rozdelene podla indexov headers_of_weeks (bez nich)

    for i in range(len(indexes) - 1):
        weeks_dict[headers_of_weeks[i][0]] = []
        for n in range(indexes[i+1] - indexes[i]):
            weeks_dict[headers_of_weeks[i][0]].append(data[indexes[i]+n])
    
    for key in weeks_dict.keys():
        print(key)

    return data, headers_of_weeks, weeks_dict

read_data()


'''
['1. Týždeň- 3.1.2022-9.1.2022- (87,5kg)']
['01/03/2022 1.trening', '01/06/2022 2.trening', '01/08/2022 3.trening']
['3x', '3x', '3x']
['Trapbar DL', '10x87,5kg+8x100kg+6x112,5kg', 'pohoda', 'Back Squat', '10x70kg+8x80kg+6x90kg', 'pohoda', 'SLRDL', '8x30kg', 'pohoda']
['Plank', '30 sec.', 'Slides plank', '8x', 'obyc plank som dal', 'Fitball plank', '30 sec.']
['Landmine press SA', '12x30kg', 'pomerne tazke', 'Lat pulldown SA', '12x35kg', 'pohoda', 'Handstand push up', '5x', 'mega problem']
['3x', '3x', '3x']
['Lunges', '8x40kg', 'tazke velmi', 'SL Reverse glute bridge', '6x', 'excentricka len', 'Landmine squat ', '8x40kg', '4-1-2-2']
['Autralian pull ups', '8x20kg', '8x15kg', 'Bench press', '8x70kg', 'poslednu som dal 11x70kg', 'DB Row', '8x27,5kg', 'Isiel som landmine row']
['3x', '3x', '3x']
['Calves', '15x', 'unilateral 16kg', 'Biceps', '12x', 'kladka unilateral', 'Calves', '15x']
['Shoulders', '12x', 'lu xiaojun latearal raises', 'Triceps', '12x', 'kladka unilateral', 'Shoulders', '12x', 'zadne delty']
['2. Týždeň- 10.1.2022-16.1.2022 (87,3kg)']
['01/10/2022 4.trening', '01/12/2022 1.trening', '01/14/2022 2.trening']
['3x', '3x', '3x']
['Bulg. Split squat', '8x40kg', 'pohoda', 'Trapbar DL', '10x92,5kg+8x105kg+6x117,5kg', 'tazke', 'Back Squat', '10x72,5kg+8x82,5kg+6x92,5kg', 'dobre som sa citil']
['Slides plank', '8x', 'Plank', '30 sec.', 'Slides plank', '8x']
['Neutral Pull up', '8x', 'akurat', 'Landmine press SA', '12x30kg+yellow theraband', 'tazke, posledna 8op', 'Lat pulldown SA', '12x35kg+yellow theraband', 'pohoda']
['3x', '3x', '3x']
['RDL', '8x40kg', 'pohoda', 'Lunges', '8x40kg', 'tazke', 'SL Reverse glute bridge', '6x', 'akurat']
['Push up', '8x15kg', 'pohoda', 'Autralian pull ups', '9x15kg', 'akurat', 'Push ups', '9x15kg', 'akurat']
['3x', '3x', '3x']
['Biceps', '10x12,5kg', 'hammers dumbells', 'Calves SL', '12x6kg', 'Biceps', '12x35kg', 'kladka bilateral']
['Triceps', '10x10kg', 'french press dumbells', 'Shoulders', '8x8kg', 'polyquin lateral raises', 'Triceps', '12x29kg', 'kladka bilateral']
['3. Týždeň- 17.1.2022-23.1.2022']
['01/17/2022 3.trening', '1/17/2022 4.trening', '1/22/2022 1.trening']
['3x', '3x', '3x']
['SLRDL', '8x35kg', 'dobre', 'Bulg. Split squat', '8x45kg', 'akurat', 'Trapbar DL', '10x95kg+8x107,5kg+120kg']
['Fitball plank', '30 sec.', 'Slides plank', '8x', 'Plank', '30 sec.']
['Handstand push up', '1x,1x,2x', 'robil som na bosu a slo to', 'Neutral Pull up', '9x', '9,9,7', 'Landmine press SA', '10x32,5kg']
['3x', '3x', '3x']
['Landmine squat ', '10x40kg', 'goblet 10x27,5kg', 'RDL', '10x40kg', 'dobre', 'Lunges', '8x45kg']
['DB Row', '10x27,5kg', '10x', 'DB Bench press', '8x25kg', 'dobre', 'Autralian pull ups', '12x20kg']
['3x', '3x', '3x']
['Calves', '15x', 'jezkovia', 'Biceps', '12x', 'Calves', '15x']
['Shoulders', '12x', 'zadne delty', 'Triceps', '12x', 'Shoulders', '12x']
['4. Týždeň- 24.1.2022-30.1.2022']
['1/25/2022 2.trening', '1/26/2022 3.trening', '1/29/2022 4.trening']
['3x', '3x', '3x']
['Back Squat', '10x75kg+85kg+6x95kg', 'SLRDL', '8x40kg', 'Bulg. Split squat', '8x50kg', 'akurtá']
['Slides plank', '8x', 'Fitball plank', '30 sec.', 'Slides plank', '8x']
['Lat pulldown SA', '10x41kg', 'Handstand push up', '2x', 'Neutral Pull up', '8x3kg', 'ťažké']
['3x', '3x', '3x']
['SL Reverse glute bridge', '10x', 'Landmine squat ', '8x45kg', 'RDL', '10x40kg', 'pohoda']
['Push up', '10x15kg', 'KB Row', '8x30kg', 'DB Bench press', '9x27,5kg', 'dal som 10x25kg']
['3x', '3x', '3x']
['Biceps', '12x', 'Calves', '15x', 'Biceps', '12x']
['Triceps', '12x', 'Shoulders', '12x', 'Triceps', '12x']
['5. Týždeň- 31.1.2022-6.2.2022']
['2/1/2022 1.trening', '2/3/2022 2.trening', '2/5/2022 3.trening']
['3x', '3x', '3x']
['Trapbar DL', '10x97,5kg+8x110kg+6x122,5kg', 'Back Squat', '10x77,5kg+87,5kg+6x97,5kg', 'SLRDL', '10x40kg']
['Plank', '30 sec.', 'Slides plank', '8x', 'Fitball plank', '30 sec.']
['Landmine press SA', '8x35kg', 'Lat pulldown SA', '12x32kg', 'Handstand push up', '2x,3x,3x']
['3x', '3x', '3x']
['Lunges', '10x45kg', 'SL Reverse glute bridge', '11x', 'Landmine squat ', '10x45kg']
['Autralian pull ups', '12x25kg', 'Push up', '8x20kg', 'DB Row', '9x30kg']
['3x', '3x', '3x']
['Calves', '15x', 'Biceps', '12x', 'Calves', '15x']
['Shoulders', '12x', 'Triceps', '12x', 'Shoulders', '12x']
'''