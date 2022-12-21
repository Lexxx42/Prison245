import json
import tkinter as tk
import tkinter.filedialog as fd


def pechat_v_file(employees: dict, prisoners: dict):
    employees = json.dumps(employees)

    new_file = fd.asksaveasfile(title="Сохранить файл",
               defaultextension=".txt",filetypes=(("txt файл", "*.txt"),))

    if new_file:
        new_file.write(employees)
        new_file.close()

    prisoners = json.dumps(prisoners)

    new_file = fd.asksaveasfile(title="Сохранить файл",
               defaultextension=".txt",filetypes=(("txt файл", "*.txt"),))

    if new_file:
        new_file.write(prisoners)
        new_file.close()


