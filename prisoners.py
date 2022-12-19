from logger import logging
import json
from random import randint


def print_prisoners(type_of_print):
    useful = ''
    if type_of_print == 'console':
        for i in range(len(PRISONERS_LIST.get("prisoners"))):
            useful += "id : " + PRISONERS_LIST.get("prisoners")[i]["id"]+'; ' + 'name : ' + PRISONERS_LIST.get(
                "prisoners")[i]["name"]+'; '+'surname : ' + PRISONERS_LIST.get("prisoners")[i]["second_name"]+'; ' + 'block : ' + PRISONERS_LIST.get("prisoners")[i]["area"]["name"]+'; ' + 'cell : ' + PRISONERS_LIST.get("prisoners")[i]["area"]["cell"]+'; ' + 'reason : ' + PRISONERS_LIST.get("prisoners")[i]["reason"]+'; ' + 'status : ' + PRISONERS_LIST.get("prisoners")[i]["status"]+'; ' + '\n'
        print(useful)
    elif type_of_print == 'file':
        for i in range(len(PRISONERS_LIST.get("prisoners"))):
            useful += "id : " + PRISONERS_LIST.get("prisoners")[i]["id"]+'; ' + 'name : ' + PRISONERS_LIST.get(
                "prisoners")[i]["name"]+'; '+'surname : ' + PRISONERS_LIST.get("prisoners")[i]["second_name"]+'; ' + 'block : ' + PRISONERS_LIST.get("prisoners")[i]["area"]["name"]+'; ' + 'cell : ' + PRISONERS_LIST.get("prisoners")[i]["area"]["cell"]+'; ' + 'reason : ' + PRISONERS_LIST.get("prisoners")[i]["reason"]+'; ' + 'status : ' + PRISONERS_LIST.get("prisoners")[i]["status"]+'; ' + '\n'
        return useful


def set_prisoner_id():
    max_id = 0
    for i in PRISONERS_LIST.get("prisoners"):
        if int(i.get("id")) > max_id:
            max_id = int(i.get("id"))
    print('max pr id', max_id)
    return max_id + 1


def get_current_prisoner_block(id_for_search) -> str:
    found_block = ''
    for i in PRISONERS_LIST.get("prisoners"):
        if int(i.get("id")) == id_for_search:
            area = i.get("area")
            found_block = area.get("name")
            print(found_block)
            if found_block == 'Block A':
                return 'A'
            return 'B'


def load_from_file():
    with open('data_prisoners.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


def change_prisoner_data(id_prisoner, data_for_change):
    if data_for_change.isalpha():
        print('letter')
        for i in PRISONERS_LIST.get("prisoners"):
            if int(i.get("id")) == id_prisoner:
                area = i.get("area")
                area['name'] = data_for_change
                if data_for_change == 'A':
                    area['cell'] = str(randint(1, 100))
                else:
                    area['cell'] = str(randint(101, 200))
                print('new list', PRISONERS_LIST)
    else:
        print('number')
        for i in PRISONERS_LIST.get("prisoners"):
            if int(i.get("id")) == id_prisoner:
                area = i.get("area")
                area['cell'] = data_for_change
                print('new list', PRISONERS_LIST)


def free_prisoner(p_id):
    for i in PRISONERS_LIST.get("prisoners"):
        if int(i.get("id")) == p_id:
            i['status'] = 'free'
            print('new list', PRISONERS_LIST)


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
    print(PRISONERS_LIST)


PRISONERS_LIST = load_from_file()  # текущие заключенные

