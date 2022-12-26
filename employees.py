import json
from w_r_file import update_json
from logger import logging
from pechat_v_file import pechat_v_file_employees
from prettytable import PrettyTable


# ключи - id_работника
# значения из README.md

def print_employees(type_of_print):
    if type_of_print == 'console':
        employees_table = PrettyTable()
        employees_table.field_names = ["id", "name", "salary_amount", "salary_currency", "job", "city", "street",
                                       "building",
                                       "home_phone",
                                       "mobile_personal", "status"]
        for employee in EMPLOYEES_LIST.get("employees"):
            list_row = []
            for key in employee:
                if key == "salary":
                    list_row.append(employee[key]['amount'])
                    list_row.append(employee[key]['currency'])
                elif key == "address":
                    list_row.append(employee[key]['city'])
                    list_row.append(employee[key]['street'])
                    list_row.append(employee[key]['building'])
                elif key == "contacts":
                    list_row.append(employee[key]['home_phone'])
                    list_row.append(employee[key]['mobile_personal'])
                else:
                    list_row.append(employee[key])
            employees_table.add_row(list_row)
        print(employees_table)
        logging.info("data printed to console: employees")
    elif type_of_print == 'file':
        pechat_v_file_employees(EMPLOYEES_LIST)


def set_employee_id():
    current_employees_data = load_from_file()
    max_id = 0
    for i in current_employees_data.get("employees"):
        if int(i.get("id")) > max_id:
            max_id = int(i.get("id"))
    logging.info(f"new employee id = {max_id + 1}")
    return str(max_id + 1)


def load_from_file():
    with open('data_employees.json', encoding='utf-8') as file:
        data = json.load(file)
    logging.info("Read from file employees")
    return data


def free_employee(e_id):
    for i in EMPLOYEES_LIST.get("employees"):
        if int(i.get("id")) == e_id:
            i['status'] = 'fired'
            print(f"Employee with id = {e_id} is fired now")
            update_json("employees", EMPLOYEES_LIST)
            logging.info(f"employee with id = {e_id} is fired now")


def delete_employ(e_list: dict, id_empl: int):
    new_spis = e_list
    for i in range(len(new_spis.get("employees"))):
        if int(new_spis.get("employees")[i]["id"]) == id_empl:
            new_spis["employees"][i]["status"] = e_list["employees"][i]["status"].replace("working", "fired")
    print(f"Employee with id = {id_empl} is fired now")
    update_json("employees", EMPLOYEES_LIST)
    logging.info(f"employee with id = {id_empl} is fired now")


def employee_update(emp_id, type_of_upd, new_value):
    if type_of_upd == 'salary':
        for i in EMPLOYEES_LIST.get("employees"):
            if int(i.get("id")) == emp_id:
                salary = i.get("salary")
                salary['amount'] = new_value
                update_json("employees", EMPLOYEES_LIST)
                logging.info(f"employee_update: salary amount = {new_value}")
    elif type_of_upd == 'mobile_phone':
        for i in EMPLOYEES_LIST.get("employees"):
            if int(i.get("id")) == emp_id:
                contacts = i.get("contacts")
                contacts['mobile_personal'] = new_value
                update_json("employees", EMPLOYEES_LIST)
                logging.info(f"employee_update: contacts mobile_personal = {new_value}")
    elif type_of_upd == 'home_phone':
        for i in EMPLOYEES_LIST.get("employees"):
            if int(i.get("id")) == emp_id:
                contacts = i.get("contacts")
                contacts['home_phone'] = new_value
                update_json("employees", EMPLOYEES_LIST)
                logging.info(f"employee_update: contacts home_phone = {new_value}")


def add_new_employee(tuple_employee_info):
    new_employee = {}
    new_employee["id"] = tuple_employee_info[0]
    new_employee["name"] = tuple_employee_info[1]
    new_employee["second_name"] = tuple_employee_info[2]
    new_employee["salary"] = {
        "amount": tuple_employee_info[3], "currency": tuple_employee_info[4]}
    new_employee["type"] = tuple_employee_info[5]
    new_employee["address"] = {
        "city": tuple_employee_info[6], "street": tuple_employee_info[7], "building": tuple_employee_info[8]}
    new_employee["contacts"] = {
        "home_phone": tuple_employee_info[9], "mobile_personal": tuple_employee_info[10]}
    new_employee["status"] = tuple_employee_info[11]
    EMPLOYEES_LIST.get("employees").append(new_employee)
    update_json("employees", EMPLOYEES_LIST)
    logging.info(f"employee added to stuff with id = {tuple_employee_info[0]}")


EMPLOYEES_LIST = load_from_file()  # текущие работники
