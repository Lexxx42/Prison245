from prisoners import PRISONERS_LIST
from employees import EMPLOYEES_LIST
from logger import logging


def write_file_prisoners(data_for_write):
    with open('prisoners.txt', 'w') as prisoners_data:
        prisoners_data.write(data_for_write)
        logging.info("data written to file: {}".format(data_for_write))


def write_file_employees(data_for_write):
    with open('employees.txt', 'w') as employees_data:
        employees_data.write(data_for_write)
        logging.info("data written to file: {}".format(data_for_write))
