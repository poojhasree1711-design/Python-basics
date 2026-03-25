#set is mutable,unordered and dont allows duplicates

set1={1,2,3,3,2,3}
print(set1)

#add,update
set2={23,45,83,97}
set3={"girl","boy","man","woman"}
print(set2,set3)

set2.add(33)
#adding of value into the set
print(set2)

set2.update(set3,set1)
#updating one set with addition of another set 
print(set2)

set3.update([9,452])
#updating a set or adding element into the set
set2.update(set1,set3)
#we can add multiple set into a set by update method
print(set2)

#remove,discard,pop
set4={"tree",34,3.221,567,"color",45.7,"pen"}
print(set4)

# set4.remove(35)-return error if tbe element is not found
set4.remove(34)
#remove if it is in the set

set4.discard("colors")
#doesn't show any error even if the element is not found 
set4.discard("color")
print(set4)

set4.pop()
#pops a random element because set is unordered
print(set4)

#clear
set4.clear()
print(set4)
#returns empty set [set()] like this

#union,intersection
set5={1,2,3,"rose","lily"," tulip"}
set6={"rose","tulip","Lily",5,4,2.0}

print(set5.union(set6))
#returns all ghe values in the sets

print(set6.intersection(set5))
#returns the same elelment btw two sets
#here the reason why tulip and lily didnt get printed because set is a case sensitive and it also matters the space.

print(set5.difference(set6))
print(set6.difference(set5))
#returns the value in first set which is not in second set

#issubset,issuperset,isdisjoint
set7={3,4,6,8}
set8={7,2,5,9}
set9={3,4,6,8}
set10={7,2}
print(set7.isdisjoint(set8))
#returns true because they din't have any common elements
print(set9.isdisjoint(set7))
#returns false because they do have same elemnts

print(set10.issubset({7,2,5,5}))
#returns true if the elements that are present in first mentioned set are also in second mentioned set(it needs to contain all the elements in the first set)

print(set8.issubset(set10))
#returns false because set8 doesnt only contains elements common with set10, it also have different elements

print(set7.issuperset(set9))
#returns true because set7 contains all the elements in set 9

print(set7.issuperset({3,4,6,5,8}))
#returns false because the set7 doesn't contains ALL the elements

#the viewing perspective only gives difference btw issubset() and issuperset()