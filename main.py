from user_interface import main_menu, free_prisoner_ui, fire_an_employee_ui, add_new_prisoner_ui, add_new_employee_ui, \
    change_prisoner, change_employee
from logger import logging
from prisoners import print_prisoners
from employees import print_employees
from w_r_file import write_file_prisoners
from w_r_file import write_file_employees


def main():
    logging.info('Start program.')
    operation_type, operation_code = main_menu()
    print(operation_type, operation_code)
    options(operation_type, operation_code)
    logging.info('Session finish')


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
            result = 'Empty'
            logging.info('Something went really wrong!')


def operations(t_opt, opt):
    match t_opt, opt:
        case 1, 1:
            print('Печать в консоль списка заключенных')
            print_prisoners()
        case 1, 2:
            print('Печать в файл списка текущих заключенных')
            write_file_prisoners()
        case 1, 3:
            print('Добавление нового заключенного в тюрьму')
            add_new_prisoner_ui()
        case 1, 4:
            print('Освобождение заключенного из тюрьмы')
            free_prisoner_ui()
        case 1, 5:
            print('Изменение данных заключенного')
            change_prisoner()
        case 2, 1:
            print_employees()
            print('Печать в консоль списка работников')
        case 2, 2:
            print('Печать в файл списка текущих работников')
            write_file_employees()
        case 2, 3:
            print('Добавление нового работника')
            add_new_employee_ui()
        case 2, 4:
            print('Увольнение работника')
            fire_an_employee_ui()
        case 2, 5:
            print('Изменение данных работника')
            change_employee()


if __name__ == '__main__':
    main()
