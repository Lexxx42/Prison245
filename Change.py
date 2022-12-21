import json

def change_employees_data_sal(id_employees, data_for_change):
    with open('data_employees.json', encoding='utf-8') as f:
        data = json.load(f)
        for i in data.get("employees"):
            if int(i.get("id")) == id_employees:
                salary = i.get("salary")
                salary['amount'] = data_for_change
            with open('data_employees.json', 'w') as f:
                json.dump(data, f)
# change_employees_data_sal(73894058, 55000)

def change_employees_data_h_ph(id_employees, data_for_change):
    with open('data_employees.json', encoding='utf-8') as f:
        data = json.load(f)
        for i in data.get("employees"):
            if int(i.get("id")) == id_employees:
                contacts = i.get("contacts")
                contacts['home_phone'] = data_for_change
            with open('data_employees.json', 'w') as f:
                json.dump(data, f)

def change_employees_data_mob_per(id_employees, data_for_change):
    with open('data_employees.json', encoding='utf-8') as f:
        data = json.load(f)
        for i in data.get("employees"):
            if int(i.get("id")) == id_employees:
                contacts = i.get("contacts")
                contacts['mobile_personal'] = data_for_change
            with open('data_employees.json', 'w') as f:
                json.dump(data, f)
 
# change_employees_data_mob_per(73894058, 11111111111)
import json
  
def change_prisoner_data_cell(id_prisoner, data_for_change):
    with open('data_prisoners.json', encoding='utf-8') as f:
        data = json.load(f)
        for i in data.get("prisoners"):
            if int(i.get("id")) == id_prisoner:
                area = i.get("area")
                area['cell'] = data_for_change
            with open('data_prisoners.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

def change_prisoner_data_area_name(id_prisoner, data_for_change):
    with open('data_prisoners.json', encoding='utf-8') as f:
        data = json.load(f)
        for i in data.get("prisoners"):
            if int(i.get("id")) == id_prisoner:
                area = i.get("area")
                area['name'] = data_for_change
            with open('data_prisoners.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

# change_prisoner_data_area_name(1, 'Block B')   