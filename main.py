from user_interface import free_prisoner_ui, fire_an_employee_ui, add_new_prisoner_ui, add_new_employee_ui, \
    change_prisoner, change_employee
from logger import logging
from prisoners import print_prisoners, change_prisoner_data
from employees import print_employees
from add_data import adding_prisoner
from add_data import adding_empl


def options(type_opt, option):
    match type_opt:
        case 1:
            logging.info('Operation with prisoners.')
            operations(type_opt, option)
        case 2:
            logging.info('Operation with employees.')
            operations(type_opt, option)
        case _:
            print('Something went really wrong!')
            logging.info('Something went really wrong!')


def operations(t_opt, opt):
    match t_opt, opt:
        case 1, 1:
            print_prisoners('console')
        case 1, 2:
            print_prisoners('file')
        case 1, 3:
            new_prisoner_info = add_new_prisoner_ui(t_opt)
            adding_prisoner(new_prisoner_info)
        case 1, 4:
            free_prisoner_ui()
        case 1, 5:
            id_prisoner, item_for_change = change_prisoner()
            change_prisoner_data(id_prisoner, item_for_change)
        case 2, 1:
            print_employees('console')
        case 2, 2:
            print_employees('file')
        case 2, 3:
            new_employee_info = add_new_employee_ui(t_opt)
            adding_empl(new_employee_info)
        case 2, 4:
            fire_an_employee_ui()
        case 2, 5:
            change_employee()



