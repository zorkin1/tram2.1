import csv
import os
#функция определения максимального количества строк в csv файле
#пример
    #import fu
    #fu.max_line_file_csv('mgt_example_trans.csv')

def max_line_file_csv(file):
    with open(file) as file_csv:
        reader = csv.DictReader(file_csv, delimiter=";")
        p = os.path.abspath('file_csv')
        print('Функция поиска максимального количества строк в файле запушена, ждите')
        for row in reader:
            pass
        print('Максимальное количество строк в файле',p,'-', reader.line_num)
        i=reader.line_num
    return (i)

#max_line_file_csv('mgt_example_trans.csv')
