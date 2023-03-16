import csv
import os
import pandas as pd
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
def xlsx_to_csv_pd():
#функция преобразования xls файла в scv
    data_xls = pd.read_excel('C:/tram/справочник.xlsx', index_col=0)
    data_xls.to_csv('C:/tram/справочник_xlsx_to_csv.csv', encoding='cp1251', sep=';')


if __name__ == '__main__':
    xlsx_to_csv_pd()


#max_line_file_csv('mgt_example_trans.csv')
