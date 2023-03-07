import openpyxl
import csv

find_vagon=0
no_find_vagon=0
no_data=0
print('Поиск')
with open('mgt_example_trans.csv') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        row = str(row['PSG_DEVICE'])
        row_find = row
#        print(row_find)

        book = openpyxl.open("справочник.xlsx", read_only=True)
        sheet = book.active
        count = 0
        validator = []
        for i in sheet.values:
            count += 1
            i = str(i)
            x = i.find(row_find)
            if x > 0:

#                print('Вагон', row, 'найден в строке', count)
                validator.append(i)
                print(validator)
                find_vagon+=1
                print({find_vagon}, {no_find_vagon}, {no_data})

            elif x ==-1:
#               print(x, 'Вагон', row_find, 'не найден в строке', count)
               no_find_vagon+=1
            else:
                pass
                no_data+=1
                print('Нулевое значение')

print('Найдено', find_vagon)
print('Не найдено',no_find_vagon)
print('Нет данных',no_data)