from datetime import datetime

def write_log(data, value):
    if value == 'w':
        edit_log(f'Recording data at {datetime.now()} | {data}\n')
    elif value == 'r':
        edit_log(f'Research data at {datetime.now()} | {data}\n')
    elif value == 'd':
        edit_log(f'Delete data at {datetime.now()} | {data}\n')
    else:
        edit_log(f'Wrong input at {datetime.now()} | {data}\n')

def edit_log(text):
    with open('log.txt', 'a', encoding='UTF8') as file:
        file.write(text)
        file.close()
