import os

def delete():
    request = input('Input request: ')
    with open('data.csv', encoding='UTF8') as infile, open('data_temp.csv', "w", encoding='UTF8') as outfile:
        for line in infile:
            if request not in line:
                outfile.write(line)
    os.remove('data.csv')
    os.rename('data_temp.csv', 'data.csv')
    print('Data was delete!')
    return request





