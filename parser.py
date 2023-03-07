import csv
from find_PSG_DEVICE import fing_validator
validator = ()

with open('C://tram/mgt_example_trans.csv') as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        print(row['PSG_DEVICE'])
        fing_validator(str(row)
            print(validator)