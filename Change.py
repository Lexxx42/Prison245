import json
def change_prisoner(i, key, value): # i - это индекс в списке 0 - Мария, 1 - Сергей и т.д. поряковый номер начиная с 0? так сказать, не ID
    with open('data_prisoners.json') as f:
        data = json.load(f)
        data['prisoners'][i]['area'][f'{key}'] = f'{value}'
    with open('data_prisoners.json', 'w') as f:
        json.dump(data, f)
    return data # может пригодится, чтобы сразу в консоль вывести
print(change_prisoner(0,'name', 'Block A'))   