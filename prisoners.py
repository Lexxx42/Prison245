from logger import logging
import json


def print_prisoners():
    print(PRISONERS_LIST)


def set_prisoner_id():
    current_prisoners_data = load_from_file()
    max_id = 0
    for i in current_prisoners_data.get("prisoners"):
        if int(i.get("id")) > max_id:
            max_id = int(i.get("id"))
    print('max pr id', max_id)
    return max_id + 1


def get_current_prisoner_block(id_for_search)-> str:
    current_prisoners_data = load_from_file()
    found_block = ''
    for i in current_prisoners_data.get("prisoners"):
        if int(i.get("id"))==id_for_search:
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


PRISONERS_LIST = load_from_file()  # текущие заключенные
