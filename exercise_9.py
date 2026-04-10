#JSON AND PICKLE:-
#converting python object into json string
dict_json={"name":"poojha","age":19,"dept":"IT","hobbies":("reading,writing"),"student":True,"graduated":False,"weight":43.50,"diability":None}
type(dict_json)

import json
data_1=json.dumps(dict_json)#to convert python to json
print(data_1)

data_2=json.loads(data_1)#to convert from json to python
print(data_2)

#above concept in file handling
import json
with open("data.json","w") as f:
    json.dump(dict_json,f)#dumping them into json by write mode

with open("data.json","r") as f:
    values=json.load(f)#loading them into python back by read mode
    print(values)


#converting python into pickle 
dict_pickle={"name":"poojha sree","age":19,"dept":"IT","hobbies":("reading,writing"),"student":True,"graduated":False,"weight":43.50,"diability":None}
type(dict_pickle)

import pickle
with open("log.pkl","wb") as f:
    pickle.dump(dict_pickle,f)#dumping into pickle

with open("log.pkl","rb") as f:
    data_saved=pickle.load(f)#loading as python back
    print(data_saved)
