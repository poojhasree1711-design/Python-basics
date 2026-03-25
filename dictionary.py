#dictionary
TBR={"Book":"Metamorphsis",
"Price":200,
"Author":"Franz Kafka",
"Pages":84,
}
print(TBR)

#returns value of a particular key or accesssing values
print(TBR["Book"],TBR["Author"])

#if the key isnt in dictionary, it will show error
#print(TBR["publication"])-this will return error

# but by accesssing values using get(), it wont show error 
print(TBR.get("Book"))
print(TBR.get("publications"))

#adding/updating the keys and values
#adding
TBR["Words"]="21,000 to 23,000 approx"
print(TBR)

#updating
TBR["Pages"]=70
print(TBR)

#to remove or delete in dictionary we use,
#pop-removes a specific key
print(TBR.pop("Pages"))
print(TBR)

#popitem-pops the last inserted item
print(TBR.popitem())
print(TBR)

#delete-delete the specific
del TBR["Book"]

#clear-clears or pops everything from the specified dictionary
print(TBR.clear())

#keys()-returns the keys in the dictionary
print(TBR.keys())

#values()-returns values of the keys implied
print(TBR.values())

##items-returns the pairs present in the dictionary
print(TBR.items())

#2-dictionary
std_details={"name":"Pooja",
"dept":"IT",
"ID":110}
print(std_details)

#adding keys
std_details["age"]=20
print(std_details)

#pop/del
del std_details["dept"]
print(std_details)


#looping through dictionary
#3-dictionary
library={"Book":"Metamorphsis",
"Price":200,
"Author":"Franz Kafka",
"Pages":84,}
print(library)

#looping through keys
for key in library:
    print(key) 
    #or
for keys in library.keys():
    print(keys)    

#looping through values
for value in library:
    print(value)
    #or
for values in library.values():
    print(values) 

#looping through both keys and values
for key,value in library.items():
    print(key,":",value)  

#if/else conditions
for key,value in library.items():
    if key=="Author":
        print("the values:",value)
    else:
        print("the key",key,"does not have specified value") 

#finding max/min in dictionary using if,else conditions
d = {"a": 10, "b": 25, "c": 5, "d": 25}
max=max(d.values())
print(max)
for key,value in d.items():
    if value==max:
        print("the keys:", key)
    else:
        print("the keys",key,"does not have highest value")    