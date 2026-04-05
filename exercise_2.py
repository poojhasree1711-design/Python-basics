#FIZZBUZZ METHOD
num=int(input("enter the number:"))
if (num%3==0):
     print("Fizz")
if(num%5==0):
     print("Buzz")
if(num%3==0 and num%5==0):
     print("FizzBuzz")          
else:
    print("no FizzBuzz")     

#SORTING A LIST OF STRINGS BY LENGTH
#1->
list=["apple","play","numbers","toy","z"]
result=sorted(list,key=len) #here, sorting the list of strings based on the length of each string in ascending order
print(result)

#2->
list=["apple","play","numbers","toy","z"]
result=sorted(list,key=len,reverse=True) #here, sorting the list of strings based on the length of each string in descending order
print(result)

#REVERSING A NUMBER BY LOOPING CONDITION
num=123
reverse=0
while num>0:
    digit=num%10 #mod10-returns the last digit of the number
    reverse=reverse*10+digit
    num=num//10 #floor divsion of 10-returns the number without decimal so, 
    #it removes automatically removes the last digit and give remianing digit
print(reverse)



