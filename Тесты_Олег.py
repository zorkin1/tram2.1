from _csv import writer

import fu

import csv


# fu.max_line_file_csv('C:/tram/mgt_trans_01032023.csv')
# max_line=fu.max_line_file_csv('mgt_example_trans.csv')

# i = 4267343/500000
# print (i)

max_line_in_file = 10
with open('C:/tram/mgt_example_trans.csv') as file_csv, open('C:/tram/new_file.csv', 'w') as f:
    reader = csv.reader(file_csv, delimiter=";")
    file_writer = csv.writer(f, delimiter=";")
    for row in reader:
        pass
        writer_object = writer(f, delimiter=";")
        writer_object.writerow(row)
        print((writer_object))
        if reader.line_num == max_line_in_file: break



print('программа завершена, выведено строк ', max_line_in_file)

#    writer = csv.writer(f)
#   for row in data:
#       writer.writerow(row)
