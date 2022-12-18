# Prison245

## prisoners.py

* заключенные - словарь
* ключи словаря: id заключенного, статус, ФИО, номер камеры, тюремный блок,
* статья, возраст, пол, категория камеры, хобби

### функции

* prisoners_add()
* prisoners_delete()
* prisoners_change()
* prisoners_print()

## employees.py

* сотрудники - словарь
* ключи словаря: id сотрудника, статус, ФИО, должность, возраст,
* пол, номер телефона, адрес, зарплата, стаж работы, хобби

1. номер телефона - словарь. Ключи: рабочий, личный

### функции

* employees_add()
* employees_delete()
* employees_change()
* employees_print()

## user_interface.py

* приветствие
* меню

1. работа с сотрудниками
2. работа с заключенными
3. выход из программы

* подменю с сотрудниками

11. Вывести полный список сотрудников в файл employees.txt - employees_print()
12. Добавить нового сотрудника - employees_add()
13. Уволить сотрудника - employees_delete() (изменить статус сотрудника)
14. Изменить данные о сотруднике - employees_change()

# печать в консоль закл/раб

# печать в файл закл/раб

# добавление в словарь закл/сотр
* функция, которая принимает значения в количестве, как в json файле.
* связка ключ-значения будет такая же, как в json файле, с такой же последовательностью


# увольнение работника/освобождение закл
* функция изменения статуса
* принимает id и меняет статус

# изменение заключенного/работника
* принимаем ключ, который хотим изменить и новое значение по этому ключу
* cell или name в словаре area - заключенные
* сотрудники: в словаре salary принимаем amount, currency.
* сотрудники: в словаре contacts: mobile_personal, home_phone
