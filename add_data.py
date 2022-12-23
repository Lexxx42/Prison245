from prisoners import PRISONERS_LIST
from employees import EMPLOYEES_LIST
from w_r_file import update_json
from logger import logging


def adding_empl(new_data):
    data = {}
    data["id"] = new_data[0]
    data["name"] = new_data[1]
    data["salary"] = {"amount": new_data[3], "currency": new_data[4]}
    data["type"] = new_data[5]
    data["address"] = {"city": new_data[6], "street": new_data[7], "building": new_data[8]}
    data["contacts"] = {"home_phone": new_data[9], "mobile_personal": new_data[10]}
    data["status"] = new_data[11]

    EMPLOYEES_LIST.get("employees").append(data)
    update_json("employees", EMPLOYEES_LIST)
    logging.info(f'adding employee id -> {data["id"]}, name -> {data["name"]}')


def adding_prisoner(new_data):
    data = {}
    data["id"] = new_data[0]
    data["name"] = new_data[1]
    data["second_name"] = new_data[2]
    data["area"] = {"cell": new_data[4], "name": new_data[3]}
    data["reason"] = new_data[5]
    data["status"] = new_data[6]

    PRISONERS_LIST.get("prisoners").append(data)
    update_json("prisoners", PRISONERS_LIST)
    logging.info(f'adding prisoner id -> {data["id"]}, name -> {data["name"]}')
