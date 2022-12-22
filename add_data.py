from user_interface import add_new_prisoner_ui
from prisoners import PRISONERS_LIST
from employees import EMPLOYEES_LIST
from w_r_file import update_json


#
# return (employee_id, employee_name, employee_second_name, employee_salary_amount,
# employee_salary_currency, employee_type, employee_address_city, employee_address_street,
# employee_address_building, employee_contacts_home_phone, employee_contacts_mobile_personal, employee_status)


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
    update_json("employees", data)


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


new_data = ("023", "bob", "log", "Block A", "23", "Жестокое обращение с функциями", "in jail")

adding_prisoner(new_data)

# new_data_2 = ("023", "bob", "valeeva", "90", "rub", "saint", "moscow", "yasnaya", "3", "F1", "G2", "g1")
#
# adding_empl(new_data_2)
