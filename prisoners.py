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


def load_from_file():
    with open('data_prisoners.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


PRISONERS_LIST = load_from_file()  # текущие заключенные
