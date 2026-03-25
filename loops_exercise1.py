#while()
n=10
a=2
b=5
i=0
print("fibonacci series:")
while i<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1

#for()    
n=10
a=7
b=3
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#PALINDROME USING while()condition
string=input("enter the string:")
reverse=""
i=len(string)-1 #this returns the reverse of the string
while i>=0: #the condition determines that the i needs to be greater than or equal to  0 
    reverse=reverse+string[i]
    i-=1 #it decreasing the index i
if(string==reverse):
    print("palindrome")
else:
    print("no palindrome")

#PALINDROME USING slicing operator 
string_1=input("enter the string:")
if (string_1==string_1[::-1]): #here the slicing [::-1] meant [start:stop:step], start and stop has been default and -1 means reverse of the string
    print("palindrome")
else:
    print("not a palindrome")

##PALINDROME USING for()condition
string_2=input("enter the string3:")
rev=""
for char in string_2:
    rev=char+rev #here the char meant the first character of the string and the loop will continue until to check whether it is palindrome or not
if(string_2==rev):
    print("palindrome")
else:
    print("no palindrome")    

#simple calculator
while True:
 num1=int(input("enter the number:"))
 num2=int(input("enter the number:"))
 operation=input("enter the operation:")
 if(operation=="+"):
     print(num1+num2)
 elif(operation=="-"):
     print(num1-num2)
 elif(operation=="*"):
     print(num1*num2)
 elif(operation=="/"):
     print(num1/num2)
 else:
     print("invalid input")
 choice=input("do you want to continue?")
 if(choice=="n"):
     break
 else:
     continue