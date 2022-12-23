import json
import tkinter as tk
import tkinter.filedialog as fd
import pprint

def pechat_v_file(employees: dict, prisoners: dict):
    
    new_file = fd.asksaveasfilename(title="Сохранить файл c преступниками",
                defaultextension=".txt",filetypes=(("txt файл", "*.txt"),))

    file_stream = open(new_file,'w')

    Mass_Emp = prisoners['prisoners']

    iter = int(1)

    for element in Mass_Emp:
        str_print = str(iter) + ": "
        str_print = str_print + "id: " + element['id'] + "; name: " + element['name'] + "; second_name: " + element['second_name'] + "; reason: " + element['reason'] + "; status: " + element['status'] + "\n"
        print(str_print)
        file_stream.write(str_print)
        str_print = "area: " + element['area']['name'] + " - " + element['area']['cell'] + "\n"
        print(str_print)
        file_stream.write(str_print)
       
        iter = iter + 1

    file_stream.close()
    
    new_file = fd.asksaveasfilename(title="Сохранить файл с работниками",
               defaultextension=".txt", filetypes=(("txt файл", "*.txt"),))

    file_stream = open(new_file,'w')

    Mass_Emp = employees['employees']

    iter = int(1)

    for element in Mass_Emp:    
        str_print = str(iter) + ":"          
        str_print = str_print + "id: " + element['id'] + "; name: " + element['name'] + "; salary: " + str(element['salary'] ['amount']) + " " + element['salary'] ['currency'] + "; type" + element['type'] + "; address: " + element['address'] ['city'] + " " + element ['address'] ['street'] + " " + element ['address'] ['building'] + "; contacts" + element['contacts'] ['home_phone'] + " " + element['contacts'] ['mobile_personal'] + "\n"
        print(str_print)
        file_stream.write(str_print)
             
        iter = iter + 1

    file_stream.close()
    
new_file_p = fd.askopenfilename(title="Открыть файл с преступниками",
                defaultextension=".txt",filetypes=(("txt файл", "*.txt"),))

new_file_e = fd.askopenfilename(title="Открыть файл с работниками",
                defaultextension=".txt",filetypes=(("txt файл", "*.txt"),))

new_file_p = open(new_file_p, 'r', encoding='utf-8')
new_file_e = open(new_file_e, 'r', encoding='utf-8')

text1 = new_file_p.read()
prisoners= json.loads(text1)
new_file_p.close()

text1 = new_file_e.read()
employees = json.loads(text1)
new_file_e.close()

pechat_v_file(employees,prisoners)