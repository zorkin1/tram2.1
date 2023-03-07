import csv
import numpy
import openpyxl
import pandas

#функция поиска максимума строк и колонок
def max_row_colum ():

    book = openpyxl.open("C://tram/справочник.xlsx")
    sheet = book
    sheet = book.active

    rows = sheet.max_row
    cols = sheet.max_column

    print ('максимум строк', rows, 'максимум колонок', cols)

def read_csv():
    with open('C://tram/mgt_example_trans.csv') as file:
        keys = file.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in file]











