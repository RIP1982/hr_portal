import write_data as wd
import read_data as rd
import log
import delete_data as dd

def ask_user():
    choice = input('Write or read or delete data(w/r/d): ')
    if choice == 'w':
        log.write_log(wd.get_data(), 'w')
    elif choice == 'r':
        log.write_log(rd.request_data(), 'r')
    elif choice == 'd':
        log.write_log(dd.delete(), 'd')
    else:
        log.write_log('Wrong input!', choice)
        print('Wrong input!')