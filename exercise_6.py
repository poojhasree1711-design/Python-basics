#PROGRAM FOR VALUE ERROR
try:
    age=int(input("enter your age:"))
    print("my age:",age)
except ValueError:
    print("thats not a number")

#PROGRAM FOR INDEX ERROR
list=["apple","banana","pome","grapes","orange"]
try:
    index=int(input("enter index:"))
    print("element is:",list[index])
except (ValueError,IndexError) as e:
    print("error:",e)

#PROGRAM FOR WITHDRAWAL ERROR
user_balance=100
try:
    withdraw=int(input("how much do you want to withdraw?"))
    if withdraw>user_balance:
        raise ValueError("withdrawal error")
    else:
        print("withdrawn amount:",withdraw)
except ValueError as e:
    print("error:",e)
