import json
from logger import logging


def write_file_prisoners(data_for_write):
    with open('prisoners.txt', 'w', encoding='utf-8') as prisoners_data:
        prisoners_data.write(data_for_write)
        logging.info(f"data written to file: {data_for_write}")


def write_file_employees(data_for_write):
    with open('employees.txt', 'w', encoding='utf-8') as employees_data:
        employees_data.write(data_for_write)
        logging.info(f"data written to file: {data_for_write}")


def update_json(type_of_update, data):
    match type_of_update:
        case "prisoners":
            with open('data_prisoners1.json', 'w', encoding='utf-8') as file_json:
                json.dump(data, file_json, ensure_ascii=False)
        case "employees":
            with open('data_employees2.json', 'w', encoding='utf-8') as file_json:
                json.dump(data, file_json, ensure_ascii=False)
