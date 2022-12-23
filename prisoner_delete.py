def pr_1(k,m):
  new_spis = k
  for i in range(len(new_spis["prisoners"])):
    if new_spis["prisoners"][i]["id"] == m:
      new_spis["prisoners"][i]["status"] = k["prisoners"][i]["status"].replace("in jail","free")
  
  return new_spis 