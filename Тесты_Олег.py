
import pandas as pd

all_row = 0
df = pd.read_excel('C:/tram/справочник.xlsx', index_col=0)
#print(df)
print('справочник прочитан')
print('чтение строк выгрузки вылидаций')
#df_data = pd.read_csv('C:/tram/mgt_trans_01032023.csv', sep=';')

df_data = pd.read_csv('C:/tram/mgt_example_trans.csv', sep=';')
start_index = df_data.index.start
stop_index = df_data.index.stop
x = 0 T
while x < stop_index:
    data_index = df_data.iloc[x]['PSG_DEVICE']
#    print(x, 'строка - значение', data_index)
    name_file=str('find_data')+str(x)
    find_data = df.isin([data_index])

#    find_data.to_csv('C:/tram/find_data', encoding='cp1251', sep=';')
    print(find_data)
    x+= 1


print('программа завершена')
#name_file='find_data'+1

#    name_file = str('C:/tram/')+str('find_data') + str(x)
#find_data.to_csv('C:/tram/log/find_data.csv', encoding='cp1251', sep=';')
#     print_data=df_data.loc[[1], ['PSG_DEVICE']]
#     print({print_data)
#print('файл валидаций прочитан')
#all_row=df.index.stop+1
#print('В файле',all_row ,"строк")
#df.to_csv('C:/tram/new_file.csv', sep=';')
#with open('C:/tram/mgt_example_trans.csv') as file_csv, open('C:/tram/new_file.csv', 'w') as f:
#print('В файле', all_row, "строк")
#i=all_row
#print(all_row)
#print(df_data.index.stop+1)