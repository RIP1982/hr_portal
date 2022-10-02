import csv
from write_data import table

def request_data():
    request = input('Input request: ')
    with open('data.csv', encoding='UTF8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if request in line:
                discription = dict(zip(table, line))
                for key, value in discription.items():
                    print(f'{key}: {value}')
    return request

