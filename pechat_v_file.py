from exceptions import validation_enter_filename


def pechat_v_file_prisoners(prisoners: dict):
    filename = validation_enter_filename()
    source = filename + '.txt'
    file_stream = open(source, 'w', encoding='utf-8')
    mass_emp = prisoners['prisoners']
    iter_1 = int(1)
    for element in mass_emp:
        str_print = str(iter_1) + ": "
        str_print = str_print + "id: " + element['id'] + "; name: " + element['name'] + "; second_name: " + element[
            'second_name'] + "; reason: " + element['reason'] + "; status: " + element['status'] + "\n"
        file_stream.write(str_print)
        str_print = "area: " + element['area']['name'] + " - " + element['area']['cell'] + "\n"
        file_stream.write(str_print)
        iter_1 = iter_1 + 1
    file_stream.close()


def pechat_v_file_employees(employees: dict):
    filename = validation_enter_filename()
    source = filename + '.txt'
    file_stream = open(source, 'w', encoding='utf-8')
    mass_emp = employees['employees']
    iter_1 = int(1)
    for element in mass_emp:
        str_print = str(iter_1) + ":"
        str_print = str_print + "id: " + element['id'] + "; name: " + element['name'] + "; salary: " + str(
            element['salary']['amount']) + " " + element['salary']['currency'] + "; job: " + element[
                        'type'] + "; address: " + element['address']['city'] + " " + element['address'][
                        'street'] + " " + element['address']['building'] + "; contacts(home, mobile): " + \
                    element['contacts'][
                        'home_phone'] + ", " + element['contacts']['mobile_personal'] + "\n"
        file_stream.write(str_print)
        iter_1 = iter_1 + 1
    file_stream.close()
