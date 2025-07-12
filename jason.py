import json

with open("sample.json")as file_:
    data=json.load(file_)
    print(data)

map={
    "name" : "Nitish",
    "Age":25
}    

with open("sample.json", "w")as file_:
    json.dump(map,file_,indent=4)

