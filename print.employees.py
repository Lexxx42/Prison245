from logger import logging


def print_employees(type_of_print):
    useful = ''
    if type_of_print == 'console':
        for i in range(len(EMPLOYEES_LIST.get("employees"))):
            useful += "id : " + EMPLOYEES_LIST.get("employees")[i]["id"]+'; ' + 'name : ' + EMPLOYEES_LIST.get(
                "employees")[i]["name"]+'; ' + 'salary amount : ' + str(EMPLOYEES_LIST.get("employees")[i]["salary"]["amount"])+'; ' + 'salary currency : ' + EMPLOYEES_LIST.get("employees")[i]["salary"]["currency"]+'; ' + 'job : ' + EMPLOYEES_LIST.get("employees")[i]["type"]+'; ' + '\n' + 'address city : ' + EMPLOYEES_LIST.get("employees")[i]["address"]["city"]+'; ' + 'address street : ' + EMPLOYEES_LIST.get("employees")[i]["address"]["street"]+'; ' + 'address building : ' + EMPLOYEES_LIST.get("employees")[i]["address"]["building"]+'; ' + 'contacts home_phone : ' + EMPLOYEES_LIST.get("employees")[i]["contacts"]["home_phone"]+'; ' + 'contacts mobile_personal : ' + EMPLOYEES_LIST.get("employees")[i]["contacts"]["mobile_personal"]+'; ' + 'status : ' + EMPLOYEES_LIST.get("employees")[i]["status"]+'; '+'\n\n'
        logging.info("data printed to console: employees")
        print(useful)