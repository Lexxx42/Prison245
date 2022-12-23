def pr_1(k,m):
  new_spis = k
  for i in range(len(new_spis["employees"])):
    if new_spis["employees"][i]["id"] == m:
      new_spis["employees"][i]["status"] = k["employees"][i]["status"].replace("working","fired")
  
  return new_spis 