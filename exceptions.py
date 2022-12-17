""" This file is for data validation. Developed by Alexander Konukhov. """
from logger import logging

MUST_BE_INTEGER = 'Incorrect input! Input must be an integer.'
MUST_BE_A_REAL = 'Incorrect input! Input must be a real number.'
DIVISION_BY_ZERO = "Division by zero!"


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
