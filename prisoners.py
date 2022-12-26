import json
from w_r_file import update_json
from logger import logging
from random import randint
from pechat_v_file import pechat_v_file_prisoners
from prettytable import PrettyTable


def print_prisoners(type_of_print):
    prisoners_table = PrettyTable()
    if type_of_print == 'console':
        prisoners_table.field_names = ["id", "name", "surname", "block", "cell", "reason", "status"]
        for prisoner in PRISONERS_LIST.get("prisoners"):
            list_row = []
            for key in prisoner:
                if key == "area":
                    list_row.append(prisoner[key]['name'])
                    list_row.append(prisoner[key]['cell'])
                else:
                    list_row.append(prisoner[key])
            prisoners_table.add_row(list_row)
        print(prisoners_table)
    elif type_of_print == 'file':
        pechat_v_file_prisoners(PRISONERS_LIST)


def set_prisoner_id():
    max_id = 0
    for i in PRISONERS_LIST.get("prisoners"):
        if int(i.get("id")) > max_id:
            max_id = int(i.get("id"))
    logging.info(f"new prisoner id = {max_id + 1}")
    return str(max_id + 1)


def get_current_prisoner_block(id_for_search) -> str:
    for i in PRISONERS_LIST.get("prisoners"):
        if int(i.get("id")) == id_for_search:
            area = i.get("area")
            found_block = area.get("name")
            if found_block == 'Block A':
                logging.info(f"current block = {'A'} with id = {id_for_search}")
                return 'Block A'
            logging.info(f"current block = {'B'} with id = {id_for_search}")
            return 'Block B'


def load_from_file():
    with open('data_prisoners.json', encoding='utf-8') as file:
        data = json.load(file)
    logging.info("Read from file prisoners")
    return data


def change_prisoner_data(id_prisoner, data_for_change):
    if data_for_change.isalpha():
        for i in PRISONERS_LIST.get("prisoners"):
            if int(i.get("id")) == id_prisoner:
                area = i.get("area")
                area['name'] = data_for_change
                if data_for_change == 'Block A':
                    area['cell'] = str(randint(1, 100))
                else:
                    area['cell'] = str(randint(101, 200))
            update_json("prisoners", PRISONERS_LIST)
    else:
        for i in PRISONERS_LIST.get("prisoners"):
            if int(i.get("id")) == id_prisoner:
                area = i.get("area")
                area['name'] = data_for_change
    update_json("prisoners", PRISONERS_LIST)


def free_prisoner(p_id):
    for i in PRISONERS_LIST.get("prisoners", PRISONERS_LIST):
        if int(i.get("id")) == p_id:
            i['status'] = 'free'
            update_json("prisoners", PRISONERS_LIST)
            print(f"Prisoner with id = {p_id} is free now")
            logging.info(f"prisoner with id = {p_id} is free now")


def delete_pris(p_list: dict, id_pris: int):
    new_spis = p_list
    for i in range(len(new_spis.get("prisoners"))):
        if int(new_spis.get("prisoners")[i]["id"]) == id_pris:
            new_spis["prisoners"][i]["status"] = p_list["prisoners"][i]["status"].replace("in jail", "free")
    update_json("prisoners", PRISONERS_LIST)
    print(f"Prisoner with id = {id_pris} is free now")
    logging.info(f"prisoner with id = {id_pris} is free now")


def add_new_prisoner(tuple_prisoner_info):
    new_prisoner = {}
    new_prisoner["id"] = tuple_prisoner_info[0]
    new_prisoner["name"] = tuple_prisoner_info[1]
    new_prisoner["second_name"] = tuple_prisoner_info[2]
    new_prisoner["area"] = {
        "cell": tuple_prisoner_info[4], "name": tuple_prisoner_info[3]}
    new_prisoner["reason"] = tuple_prisoner_info[5]
    new_prisoner["status"] = tuple_prisoner_info[6]
    PRISONERS_LIST.get("prisoners").append(new_prisoner)
    update_json("prisoners", PRISONERS_LIST)
    logging.info(f"prisoner added to prison with id = {tuple_prisoner_info[0]}")


PRISONERS_LIST = load_from_file()  # текущие заключенные
