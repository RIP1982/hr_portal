import csv

table = ['last_name', 'name', 'phone_number', 'posts', 'salary']

def get_data():
    record = [input(f'{i}: ') for i in table]
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(record)
    print('Data was record!')
    return record



