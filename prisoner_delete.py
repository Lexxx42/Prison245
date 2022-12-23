def delete_pris(PRISONERS_LIST:dict, id_pris:int):
  new_spis = PRISONERS_LIST
  for i in range(len(new_spis.get("prisoners"))):
    if int(new_spis.get("prisoners")[i]["id"]) == id_pris:
      new_spis["prisoners"][i]["status"] = PRISONERS_LIST["prisoners"][i]["status"].replace("in jail","free")
  return new_spis  



         
