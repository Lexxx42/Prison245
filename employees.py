from logger import logging
import json


# ключи - id_работника
# значения из README.md

def print_employees():
    print(EMPLOYEES_LIST)


def set_employee_id():
    current_employees_data = load_from_file()
    max_id = 0
    for i in current_employees_data.get("employees"):
        if int(i.get("id")) > max_id:
            max_id = int(i.get("id"))
    print('max emp id', max_id)
    return max_id + 1


def load_from_file():
    with open('data_employees.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


def free_employee(e_id):
    for i in EMPLOYEES_LIST.get("employees"):
        if int(i.get("id")) == e_id:
            i['status'] = 'fired'
            print('new list', EMPLOYEES_LIST)


def employee_update(emp_id, type_of_upd, new_value):
    if type_of_upd == 'salary':
        for i in EMPLOYEES_LIST.get("employees"):
            if int(i.get("id")) == emp_id:
                salary = i.get("salary")
                salary['amount'] = new_value
                print('new list', EMPLOYEES_LIST)
    elif type_of_upd == 'mobile_phone':
        for i in EMPLOYEES_LIST.get("employees"):
            if int(i.get("id")) == emp_id:
                contacts = i.get("contacts")
                contacts['mobile_personal'] = new_value
                print('new list', EMPLOYEES_LIST)
    elif type_of_upd == 'home_phone':
        for i in EMPLOYEES_LIST.get("employees"):
            if int(i.get("id")) == emp_id:
                contacts = i.get("contacts")
                contacts['home_phone'] = new_value
                print('new list', EMPLOYEES_LIST)


EMPLOYEES_LIST = load_from_file()  # текущие работники
