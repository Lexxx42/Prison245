""" This file is for user interface. Developed by Alexander Konukhov. """
import sys
from exceptions import *
from logger import logging
from prisoners import PRISONERS_LIST, set_prisoner_id, get_current_prisoner_block
from employees import EMPLOYEES_LIST, set_employee_id


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


def add_new_prisoner_ui(type_of_operation):
    prisoner_id = set_prisoner_id()
    prisoner_name = validation_name(type_of_operation)
    prisoner_second_name = validation_surname(type_of_operation)
    print("""Available blocks in prison:
1 - Block A
2 - Block B
""")
    area_name = validation_area_name()
    area_cell = validation_area_cell(area_name)
    reason = validation_reason()
    prisoner_status = "in jail"
    print(prisoner_id, prisoner_name, prisoner_second_name,
          area_name, area_cell, reason, prisoner_status)


def add_new_employee_ui(type_of_operation):
    employee_id = set_employee_id()
    print(type_of_operation)
    employee_name = validation_name(type_of_operation)
    employee_second_name = validation_surname(type_of_operation)
    employee_salary_amount = validation_salary_amount()
    employee_salary_currency = "RUR"
    print("""Available employee positions:
1 - guard
2 - cook
3 - doctor
4 - janitor
5 - aligator feeder
""")
    employee_type = validation_employee_type()
    employee_address_city = validation_location('city')
    employee_address_street = validation_location('street')
    employee_address_building = validation_location('building')
    employee_contacts_home_phone = validation_home_phone()
    employee_contacts_mobile_personal = validation_mobile_personal()
    employee_status = "working"
    print(employee_id, employee_name, employee_second_name, employee_salary_amount, '\n',
          employee_salary_currency, employee_type, employee_address_city, employee_address_street, '\n',
          employee_address_building, employee_contacts_home_phone, employee_contacts_mobile_personal, employee_status)


def change_prisoner():
    print("""Which field do you want to edit?
1 - area name
2 - area_cell
""")
    change_mode = validation_change_prisoner()
    print_list_of_prisoners()
    if change_mode == 1:
        p_list_ids = get_list_of_prisoners_id_for_change()
        choose_id_for_edit(p_list_ids)
        id_for_edit = validation_id_for_edit(p_list_ids)
        print("id_for_edit", id_for_edit)
        print(f"""In witch block do you want to transfer the prisoner {id_for_edit}?
1 - Block A
2 - Block B
""")
        new_area_name = validation_area_name()
        print('new_area_name', new_area_name)
        return id_for_edit, new_area_name
    elif change_mode == 2:
        p_list_ids = get_list_of_prisoners_id_for_change()
        choose_id_for_edit(p_list_ids)
        id_for_edit = validation_id_for_edit(p_list_ids)
        print("id_for_edit", id_for_edit)
        print(f"""In witch block do you want to transfer the prisoner {id_for_edit}?
1 - Block A
2 - Block B
""")
        current_block = get_current_prisoner_block(id_for_edit)
        new_cell = validation_area_cell(current_block)


def print_list_of_prisoners():
    print("prisoners list")
    for i in PRISONERS_LIST.get("prisoners"):
        print(i)
    print()


def print_list_of_employees():
    print("employees list")
    for i in EMPLOYEES_LIST.get("employees"):
        print(i)
    print()


def get_list_of_prisoners_id_for_change() -> list:
    available_id_for_edit = []
    for i in PRISONERS_LIST.get("prisoners"):
        available_id_for_edit.append(i.get("id"))
    return available_id_for_edit


def choose_id_for_edit(list_for_check) -> str:
    print(f'Available ids for change: {", ".join(list_for_check)}')


def change_employee():
    print('change_employee')
