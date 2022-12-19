""" This file is for data validation. Developed by Alexander Konukhov. """
from logger import logging

MUST_BE_INTEGER = 'Incorrect input! Input must be an integer.'
MUST_BE_POSITIVE = 'Must be positive.'
MUST_BE_STRING = 'Incorrect input! Input must be a string.'
MUST_BE_GREATER_THAN_ZERO = 'Incorrect input! Input must be greater than zero.'
MUST_BE_VALID = 'Enter valid value.'


def validation_mode() -> int:
    """ Function for check user's input for main mode. """
    while True:
        try:
            calc_mode = int(input("Which mode do you need: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if calc_mode in [0, 1, 2]:
            if calc_mode == 0:
                logging.info('Finished work from main menu.')
            else:
                logging.info(f'Main mode of interface = {calc_mode}')
            return calc_mode
        print("Incorrect input! Please look at the available modes.")
        logging.exception(
            "Incorrect input! Please look at the available modes.")


def validation_operation() -> int:
    """ Function for check user's input for operation. """
    number_of_available_modes = 6
    while True:
        try:
            operation_type = int(input("Enter operation code: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'operation code = {operation_type}')
            return operation_type
        print("Incorrect input! Please look at the available operation codes.")
        logging.exception(
            "Incorrect input! Please look at the available operation codes.")


def validation_name(type_op) -> str:
    """ Function for check input for prisoner's name. """
    name = ''
    try:
        if type_op == 1:
            name = input("Enter prisoner's name: ")
        else:
            name = input("Enter employee's name: ")
            logging.info(f"employee's name = {name}")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    logging.info(f"prisoner's name = {name}")
    return name


def validation_surname(type_op) -> str:
    """ Function for check input for prisoner's surname. """
    surname = ''
    try:
        if type_op == 1:
            surname = input("Enter prisoner's surname: ")
        #else:
            #surname = input("Enter employee's surname: ")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    logging.info(f"employee's surname = {surname}")
    return surname


def validation_area_cell(block_name) -> str:
    """ Function for check input for prisoner's cell number. """
    area_cell = ''
    if block_name == 'A':
        cells = [1, 100]
    else:
        cells = [101, 200]
    while True:
        try:
            area_cell = int(input("Enter prisoner's new home (cell number): "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if block_name == 'A' and area_cell < cells[0] or area_cell > cells[1]:
            print(f"Block A have cell number from {cells[0]} to {cells[1]}")
            logging.exception(f"incorrect cell = {area_cell} in block {block_name}")
            continue
        if block_name == 'B' and area_cell < cells[0] or area_cell > cells[1]:
            print(f"Block B have cell number from {cells[0]} to {cells[1]}")
            logging.exception(f"incorrect cell = {area_cell} in block {block_name}")
            continue
        logging.info(f'selected block={block_name}, cell={area_cell}')
        return str(area_cell)


def validation_area_name() -> str:
    """ Function for check input for prisoner's block. """
    area_name = ''
    while True:
        try:
            area_name = int(input("Enter prisoner's block: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
        if area_name not in [1, 2]:
            print("Block must be available!")
            logging.exception("Block must be available!")
        else:
            if area_name == 1:
                logging.info(f"prisoner's block = {'A'}")
                return 'A'
            logging.info(f"prisoner's block = {'B'}")
            return 'B'


def validation_reason() -> str:
    """ Function for check input for prisoner's imprisonment reason. """
    p_reason = ''
    try:
        p_reason = input("Enter imprisonment reason: ")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    logging.info(f"prisoner's reason for imprisonment = {p_reason}")
    return p_reason


def validation_salary_amount() -> int:
    """ Function for check input for employee's salary amount. """
    salary_amount = 0
    max_salary_amount = 200000
    while True:
        try:
            salary_amount = int(input("How much does employee's work costs? "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
        if salary_amount > max_salary_amount:
            print("We can't afford this much!")
            logging.exception("We can't afford this much!")
        logging.info(f"employee's salary amount = {salary_amount}")
        return salary_amount


def validation_employee_type() -> str:
    """ Function for check input for employee's type. """
    employee_type = ''
    while True:
        try:
            employee_type = int(input("Enter employee's job: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
        if employee_type not in range(1, 6):
            print("Vacancy must be available!")
            logging.exception("Vacancy must be available!")
        else:
            match employee_type:
                case 1:
                    logging.info(f"employee's job = {'guard'}")
                    return 'guard'
                case 2:
                    logging.info(f"employee's job = {'cook'}")
                    return 'cook'
                case 3:
                    logging.info(f"employee's job = {'doctor'}")
                    return 'doctor'
                case 4:
                    logging.info(f"employee's job = {'janitor'}")
                    return 'janitor'
                case 5:
                    logging.info(f"employee's job = {'alligator feeder'}")
                    return 'alligator feeder'


def validation_location(location) -> str:
    """ Function for check input for employee's location. """
    check_location = ''
    try:
        check_location = input(f"Enter employee's {location}: ")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    logging.info(f"employee's location = {check_location}")
    return check_location


def validation_home_phone() -> str:
    """ Function for check input for employee's home_phone. """
    home_phone = ''
    while True:
        try:
            home_phone = int(input("Enter employee's home phone: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
        if home_phone < 0:
            print(MUST_BE_POSITIVE)
            logging.exception(MUST_BE_POSITIVE)
            continue
        logging.info(f"employee's home phone = {str(home_phone)}")
        return str(home_phone)


def validation_mobile_personal() -> str:
    """ Function for check input for employee's mobile_personal. """
    mobile_personal = ''
    while True:
        try:
            mobile_personal = int(
                input("Enter employee's mobile personal phone: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
        if mobile_personal < 0:
            print(MUST_BE_POSITIVE)
            logging.exception(MUST_BE_POSITIVE)
            continue
        logging.info(f"employee's mobile personal phone = {str(mobile_personal)}")
        return str(mobile_personal)


def validation_change(arg) -> int:
    """ Function for changing prisoner's data. """
    change_type = 0
    if arg == 'prisoner':
        while True:
            try:
                change_type = int(input("Enter change mode for prisoner: "))
            except ValueError:
                print(MUST_BE_INTEGER)
                logging.exception(MUST_BE_INTEGER)
            if change_type not in range(1, 3):
                print(MUST_BE_VALID)
                logging.exception(MUST_BE_VALID)
                continue
            return change_type
    else:
        while True:
            try:
                change_type = int(input("Enter change mode for employee: "))
            except ValueError:
                print(MUST_BE_INTEGER)
                logging.exception(MUST_BE_INTEGER)
            if change_type not in range(1, 4):
                print(MUST_BE_VALID)
                logging.exception(MUST_BE_VALID)
                continue
            return change_type


def validation_id_for_edit(available_ids):
    """ Function for changing prisoner's data. """
    available_ids = list(map(int, available_ids))
    id_for_check = ''
    while True:
        try:
            id_for_check = int(input("Enter available id: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
        if id_for_check not in available_ids:
            print(MUST_BE_VALID)
            logging.exception(MUST_BE_VALID)
            continue
        return id_for_check
