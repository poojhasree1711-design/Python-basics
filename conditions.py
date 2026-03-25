
#greatest of two numbers
a=int(input("enter the number:"))
b=24
if a>b:
    print("a is greater then b")
else:
    print("b is greater than a")

#greatest of three numbers
#if,elif,else
x=45
y=23
z=34
if x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater") 
else:
    print("z is greater")

#nested if
if x>y:
    if x>z:
      print("x is greatest")
    else:
       print("z is greatest")
else:
    if y>z:
       print("y is greatest")
    else:
       print("z is greatest")
      
#eligible to vote or not
student_age=18
if(student_age>18):
    print("eligible")
else:
    if(student_age==18):
        print("eligible")
    else:    
      print("not eligible")

#to find the integer is odd or even             
num1=int(input("enter the value:"))
if(num1%2==0):
    print("it is even")
else:
    print("it is odd")

#checking if the value has vowels
string_1=input("enter the string:")
if "a" in string_1 or "i" in string_1 or "u" in string_1 or "o" in string_1 or "u" in string_1:
    print("string contains vowels")
else:
    print("string does not contains vowels")

#leap year
#divisble by 4 and not divisble by 100 or divisble by 400 says leap year
year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("it  is a leap year")
else:
    print("it is not a leap year")

#find which list has maximum count of paritcular value
list1=[1,2,3,4,3]
list2=[1,2,3,4]
count1=list1.count(3)
count2=list2.count(3)
print(count1,count2)
if(count1>count2):
    print("list1 contains maximum occurence of 3")
else:
    if(count1<count2):
        print("list2 contains maximum occurence of 3")  
    else:
        print("both list1 and list2 has same count of 3")      
             
#to find positve or negative
number1=int(input("number:"))
if(number1>0):
    print("it is even")
else:
    print("it is odd")  


#break,continue,pass looping conditions
#stops when fruit=="banana". so we use break 
fruits=["apple","mango","banana","cherry"]
print(fruits)
for f in fruits:
    if f=="banana":
        break
    print(f)

#range from 0 to 5 using range
for a in range(6):
    print(a)    

#iterating through the word "banana"
fruit="banana"
for letter in fruit:
    print(letter)        

#break and continue conditions using range
#1
for i in range(0,11):
    if i==5:
        continue
    if i==9:
        break
    print(i)

#2
for b in range(0,21):
    if b%3==0:
        continue
    if b%11==0:
        break
    print(b)

#3
for c in range(0,16):
    if c==13:
        break
    if c%2==0:
        print("Even")
    else:
        print("Odd")
           
#using memebership operator in break/continue
word="programming"
for w in word:
    if w in "aeiou":
        continue
    if w=="g":
        break
    print(w)

#counter
count=0
for d in range(0,31):
    if d%4==0:
        count+=1
        print(d)
    if count==4:
        break    

#pass-does nothing, it is placeholder or holds error from occuring
for i in range(5):
   if i==2: 
    pass
   print(i)