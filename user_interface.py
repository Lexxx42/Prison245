""" This file is for user interface. Developed by Alexander Konukhov. """
import sys
from exceptions import *
from logger import logging
from prisoners import PRISONERS_LIST, set_prisoner_id
from employees import EMPLOYEES_LIST


def main_menu() -> None | tuple[int, int]:
    """ This function is for main menu of prison interface. """
    print("""Welcome to the 245 Prison of GB academy!


Working with:
1 - prisoners
2 - employees
0 - exit
""")

    mode = validation_mode()
    if mode == 0:
        print("We'll be glad to see you again!")
        sys.exit()
    return choose_option(mode)


def choose_option(main_mode) -> None | tuple[int, int]:
    """ This function is for available operations for chosen mode. """
    if main_mode == 1:
        print("""Prisoner operations:
1 - show current prisoners
2 - write current prisoners in a file
3 - add new prisoner
4 - free a prisoner
5 - change prisoner's data
0 - previous menu
""")
        operation = validation_operation()
    else:
        print("""Employee operations:
1 - show current employees
2 - write current employees in a file
3 - add new employee
4 - fire an employee
5 - change employee's data
0 - previous menu
""")
        operation = validation_operation()
    if operation == 0:
        return main_menu()
    else:
        return main_mode, operation


def free_prisoner_ui():
    print("Which prisoner do you want to free? ")
    # цикл вывода заключенных из PRISONERS_LIST
    # проверка значений


def fire_an_employee_ui():
    print("Which employee do you want to fire? ")
    # цикл вывода работников из EMPLOYEES_LIST
    # проверка значений


def add_new_prisoner_ui():
    prisoner_id = set_prisoner_id()
#     prisoner_name = validation_prisoner_name()
#     prisoner_second_name = validation_prisoner_surname()
#     print("""Available blocks in prison:
# 1 - Block A
# 2 - Block B
# """)
#     area_name = validation_area_name()
#     area_cell = validation_area_cell(area_name)
#     reason = validation_reason()
#     prisoner_status = set_prisoner_status()

def add_new_employee_ui():
    print('add_new_employee_ui')


def change_prisoner():
    print('change_prisoner')


def change_employee():
    print('change_employee')
