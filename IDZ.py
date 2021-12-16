# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def get_worker():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    zodiac = input("Знак зодиака: ")
    date = input("Дата: ")

    return {
        'surname': surname,
        'name': name,
        'zodiac': zodiac,
        'date': datetime.strptime(date, "%Y-%m-%d")
    }


def display_workers(staff):
    if staff:

        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} | {:^15} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Знак зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех сотрудниках.
        for idx, worker in enumerate(staff, 1):
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} | {:^15} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiac', ''),
                    str(worker.get('date', '').date())
                )
            )
        print(line)

    else:
        print("Список работников пуст.")


def select_workers(staff):
    month1 = int(input("Введите месяц: "))
    result = []
    for worker in staff:
        if worker.get('date', '').month == month1:
            result.append(worker)
    return result


def main():
    workers = []

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            worker = get_worker()

            workers.append(worker)
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            display_workers(workers)

        elif command.startswith('select'):
            selected = select_workers(workers)
            display_workers(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить запись;")
            print("list - вывести список;")
            print("select - список родившихся в один месяц;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("")


if __name__ == '__main__':
    main()
