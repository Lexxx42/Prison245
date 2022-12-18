from logger import logging
import json


def print_prisoners():
    print(PRISONERS_LIST)


def load_from_file():
    with open('data_prisoners.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


PRISONERS_LIST = load_from_file()  # текущие заключенные
