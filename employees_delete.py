def delete_employ(EMPLOYEES_LIST:dict, id_empl:int):
  new_spis = EMPLOYEES_LIST
  for i in range(len(new_spis.get("employees"))):
    if int(new_spis.get("employees")[i]["id"]) == id_empl:
      new_spis["employees"][i]["status"] = EMPLOYEES_LIST["employees"][i]["status"].replace("working","fired")
  return new_spis