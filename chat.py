import light_info
import datetime
import art
from tqdm import tqdm
from time import sleep


def greeting():
    print('Вас вітає чат курсового проекту Python Starter')


def regards():
    art.tprint('Have a nice day!', font='wiz')


def menu():
    chosen_action = int(input('Є можливість:\n'
                          '\t0 - познайомитись\n'
                          '\t1 - переглянути розклад дня\n'
                          '\t2 - переглянути розклад на тиждень\n'
                          '\t3 - перевірити наявність електроенергії\n'
                          '\t4 - додати нові активності до переліку справ\n'
                          '\t9 - вийти з чату\n'))
    match chosen_action:
        case 9: return 'quit'
        case 4: add_new_todo()
        case 3: ask_full_or_1day()
        case 2 | 1: show_todo_list()
        case 0: greeting()
        case _: print('Програма не зрозуміла Вашого вибору')



def add_new_todo():
    input('Що бажаєте записати до переліку важливих справ: ')
    for i in tqdm(range(int(5)), total=8, ncols=110, desc='Зберігаємо введену інформацію...', colour='green'):
        sleep(i)


def show_todo_list():
    print('This feature will be available after next release')


def ask_full_or_1day():
    sel_range = input('Оберіть будь ласка для якого періоду часу розклад наявності е/е Вас цікавить\n'
                      '\t0 - весь відомий розклад\n'
                      '\t1 - на сьогодні\n'
                      '\t2 - на інший день\n'
                      '\t3 - зараз\n'
                      '\t4 - інший період протягом одного дня\n')
    match sel_range:
        case 0: light_info.show_full_el_info()
        case 1: light_info.show_info_1day(datetime.date.today().isoweekday())
        case 2:
            sel_day = int(input('Введіть номер дня від 1 до 7 '))
            light_info.show_info_1day(sel_day)
        case 3:
            light_info.show_info_hours(datetime.date.today().isoweekday(), datetime.datetime.now().hour)
        case 4:
            sel_day = int(input('Введіть номер дня від 1 до 7 '))
            sel_hour_start = int(input('Введіть початкову годину періоду, що Вас цікавить '))
            sel_hour_range = int(input('Яка тривалість вибраного періоду? '))
            if sel_hour_start + sel_hour_range > 24:
                sel_hour_range = 24 - sel_hour_start
            light_info.show_info_hours(sel_day, sel_hour_start, sel_hour_range)
        case _:
            print('Програма не зрозуміла Вашого вибору')
