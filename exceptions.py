""" This file is for data validation. Developed by Alexander Konukhov. """
from logger import logging

MUST_BE_INTEGER = 'Incorrect input! Input must be an integer.'
MUST_BE_A_REAL = 'Incorrect input! Input must be a real number.'
MUST_BE_STRING = 'Incorrect input! Input must be a string.'
MUST_BE_GREATER_THAN_ZERO = 'Incorrect input! Input must be greater than zero.'


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
        logging.exception("Incorrect input! Please look at the available modes.")


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
        logging.exception("Incorrect input! Please look at the available operation codes.")


def validation_prisoner_name() -> str:
    """ Function for check input for prisoner's name. """
    p_name = ''
    try:
        p_name = input("Enter prisoner's name: ")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    return p_name


def validation_prisoner_surname() -> str:
    """ Function for check input for prisoner's surname. """
    p_surname = ''
    try:
        p_surname = input("Enter prisoner's surname: ")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    return p_surname


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
            continue
        if block_name == 'B' and area_cell < cells[0] or area_cell > cells[1]:
            print(f"Block B have cell number from {cells[0]} to {cells[1]}")
            continue
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
                return 'A'
            return 'B'


def validation_reason() -> str:
    """ Function for check input for prisoner's imprisonment reason. """
    p_reason = ''
    try:
        p_reason = input("Enter imprisonment reason: ")
    except ValueError:
        print(MUST_BE_STRING)
        logging.exception(MUST_BE_STRING)
    return p_reason
