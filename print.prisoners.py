from logger import logging



def print_prisoners(type_of_print):
    useful = ''
    if type_of_print == 'console':
        for i in range(len(PRISONERS_LIST.get("prisoners"))):
            useful += "id : " + PRISONERS_LIST.get("prisoners")[i]["id"]+'; ' + 'name : ' + PRISONERS_LIST.get(
                "prisoners")[i]["name"]+'; '+'surname : ' + PRISONERS_LIST.get("prisoners")[i]["second_name"]+'; ' + 'block : ' + PRISONERS_LIST.get("prisoners")[i]["area"]["name"]+'; ' + 'cell : ' + PRISONERS_LIST.get("prisoners")[i]["area"]["cell"]+'; ' + 'reason : ' + PRISONERS_LIST.get("prisoners")[i]["reason"]+'; ' + 'status : ' + PRISONERS_LIST.get("prisoners")[i]["status"]+'; ' + '\n'
        logging.info("data printed to console: prisoners")
        print(useful)