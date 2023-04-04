import pandas as pd    # Импорт библиотеки Pandas для работы с таблицами
import time            # Импорт библиотеки time для измерения времени выполнения скрипта
from tqdm import tqdm  # Импорт библиотеки tqdm для отображения прогресс-бара во время выполнения цикла

start = time.time()  # Запуск таймера
no_data_validor=0
# Чтение файла 'mgt_trans_01032023.csv' с разделителем ';'
# и сохранение его в DataFrame 'df_data'
df_data = pd.read_csv('C:/tram/mgt_trans_01032023.csv', sep=';')
#df_data = pd.read_csv('C:/tram/mgt_example_trans.csv', sep=';')

# Чтение файла 'справочник.scv' и сохранение его в DataFrame 'df_dire'
df_dire = pd.read_csv('C:/tram/справочник.csv', sep=';', encoding='cp1251')

# Создание пустого словаря 'data'
data = {}

# Для каждого столбца в 'df_data' и 'df_dire' добавление ключа в словарь 'data'
for i in list(df_data.columns):
    data[f'{i}'] = []
for i in list(df_dire.columns):
    data[f'{i}'] = []

# Попытка выполнить следующий блок кода.
# Если в блоке возникает исключение, то будет выведено сообщение об ошибке.
try:
    # Итерация по каждой строке в 'df_data'
    for index, row in tqdm(df_data.iterrows(), total=len(df_data)):
        # Для каждого столбца в 'df_data' добавление значения в словарь 'data'
        for key in df_data.columns:
            data[key].append(row[key])
        # Получение значения 'PSG_DEVICE' в текущей строке
        device = str(row['PSG_DEVICE'])
        # Если значение 'PSG_DEVICE' есть в 'df_dire'
        if device in df_dire.values:
            # Нахождение индекса строки в 'df_dire', где значение соответствует 'PSG_DEVICE'
            row_index = df_dire.index[df_dire.eq(device).any(axis=1)].tolist()[0]
            # Получение значений в этой строке и добавление их в словарь 'data'
            data_row = df_dire.iloc[row_index].to_dict()
            for key, value in data_row.items():
                data[key].append(value)
        # Если значение 'PSG_DEVICE' отсутствует в 'df_dire'

        else:
            # Добавление пустых значений в каждый столбец 'df_dire'
            for key in list(df_dire.columns):
                data[key].append('')
                no_data_validor = no_data_validor + 1
# Если возникла ошибка, вывод сообщения об ошибке
except Exception as e:
    print("ERROR : " + str(e))

# Преобразование словаря 'data' в DataFrame и запись его в файл 'output.csv' без индексов
df = pd.DataFrame(data)
df.to_csv('C:/tram/output.csv', index=False, encoding='cp1251', sep=';')

end = time.time()  # Остановка таймера
print(f'Завершено за {end - start:.2f}')  # Вывод времени выполнения скрипта
no_data_valid=no_data_validor/8
print('не найдено ', no_data_valid, 'валидация ')