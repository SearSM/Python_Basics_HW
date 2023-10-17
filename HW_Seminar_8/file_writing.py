'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''

from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    info = []
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    info.append(last_name)
    info.append(first_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline="") as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)


def change_info():
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        print(res)
    info_change = input('Введите, что необходимо изменить(Фамилия, Имя, Номер): ')
    old_info = input('Введите старую информацию: ')
    flag = False
    if info_change == 'Номер':
        while not flag:
            try:
                new_info = int(input('Введите новый номер телефона: '))
                if len(str(new_info)) != 11:
                    print('Неправильный номер')
                else:
                    flag = True
            except ValueError:
                print('not valid number')
    else:
        new_info = input('Введите новую информацию: ')
    with open('phone.csv', 'w', encoding='utf-8', newline="") as f_n:
        if info_change == 'Фамилия':
            for el in res:
                if el['Фамилия'] == old_info:
                    el['Фамилия'] = new_info
        elif info_change == 'Имя':
            for el in res:
                if el['Имя'] == old_info:
                    el['Имя'] = new_info
        elif info_change == 'Номер':
            for el in res:
                if el['Номер'] == old_info:
                    el['Номер'] = new_info
        else:
            print('Данные не совпадают')
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)


def delete_info():
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        print(res)
        delete_obj = input('Введите Фамилию, Имя или Номер удаляемого объекта: ')
        for el in res:
            if el['Фамилия'] == delete_obj or el['Имя'] == delete_obj or el['Номер'] == delete_obj:
                res.remove(el)
    with open('phone.csv', 'w', encoding='utf-8', newline="") as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(*read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'c':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                change_info()
        elif command == 'd':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            else:
                delete_info()


main()