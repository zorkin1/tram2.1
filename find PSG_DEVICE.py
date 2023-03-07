import openpyxl

def fing_validator(row):
    row = str(31133)
    book = openpyxl.open("C://tram/справочник.xlsx", read_only=True)
    sheet = book.active
    count=0
    validator = []
    for i in sheet.values:
        count+=1
        i = str(i)
        x = i.find(row)

        if x > 0:
            print('Вагон найден в строке', count)
            validator.append(i)
            print(validator)
        else:
            print('нет данных')

