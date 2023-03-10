
import fu
from csv import writer
import csv
import pandas as pd

# fu.max_line_file_csv('C:/tram/mgt_trans_01032023.csv')
# max_line=fu.max_line_file_csv('mgt_example_trans.csv')
# i = 4267343/500000
# print (i)

max_line_in_file = 10
#with open('C:/tram/mgt_example_trans.csv') as file_csv:
df = pd.read_csv('C:/tram/mgt_trans_01032023.csv', sep=';')
all_row=df.index.stop+1
print('В файле',all_row ,"строк")

#df.to_csv('C:/tram/new_file.csv', sep=';')

#with open('C:/tram/mgt_example_trans.csv') as file_csv, open('C:/tram/new_file.csv', 'w') as f:
#    reader = csv.reader(file_csv, delimiter=";")
#    file_writer = csv.writer(f, delimiter=";", )
#    for stroka in reader:
#        pd.to_csv('C:/tram/new_file.csv')
#        print(stroka)
#        writer_object = writer(f, delimiter=";")
#        print('writer_object', reader.line_num)
#        writer_object.writerow(stroka)
#        print('writer_object.writerow(row)', reader.line_num)

#        writer = writer(f, delimiter=";")
 #       writer.csv.writerows(row)
#       print()
#        if reader.line_num == max_line_in_file: break
print('программа завершена')

