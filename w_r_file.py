from prisoners import PRISONERS_LIST
from employees import EMPLOYEES_LIST
from logger import logging


def write_file_prisoners(data_for_write):
    with open('prisoners.txt', 'w') as prisoners_data:
        print('вывод словаря PRISONERS_LIST удобным видом в txt')
    # print(PRISONERS_LIST)


def write_file_employees():
    with open('employees.txt', 'w') as employees_data:
        print('вывод словаря EMPLOYEES_LIST удобным видом в txt')
    # print(EMPLOYEES_LIST)
