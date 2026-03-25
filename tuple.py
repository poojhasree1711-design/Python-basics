#tuple immutable,indexed,ordered,allows dupes

t1=(1)
t2=(3.14)
print(type(t1),type(t2))
#for tuple comma(,)is necessary or else it will be considered as other datatypes

tuple1=(7,)
tuple2=(5,"deer",3.77)
print(type(tuple1),type(tuple2))
#comma gives the whole meaning of tuple

#tuple is immutable
tuple3=(1,2,4)
#tuple3[1]=6
print(tuple3)
#rerurns the error because tuple dont allow to change or remove values

#count,index
tuple4=(3,7,78,5,3,4,"siren",3,3,73,4)
print(tuple4)

print(tuple4.count(3))
#returns how many times a element occured in the tuple

print(tuple4.index(78))
#returns the position of the value

print(tuple4[6])
print(tuple4[-3])
#returns the value in the particular index

#nested tuple
tuple5=(9,5,(1,"apple"),4,6)
print(tuple5)
#returns tuple inside a tuple