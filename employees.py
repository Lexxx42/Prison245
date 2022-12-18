from logger import logging
import json


# ключи - id_работника
# значения из README.md

def print_employees():
    print(EMPLOYEES_LIST)


def load_from_file():
    with open('data_employees.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


EMPLOYEES_LIST = load_from_file()  # текущие работники
