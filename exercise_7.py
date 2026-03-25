#creation of file called student.txt
file=open("student.txt","w")
file.write("Arjun\n")
file.write("Karthik\n")
file.write("Priya")
file.close()

#opening the file and reading the count of words
file=open("student.txt","r")
data=file.read()
words=data.split()
count=len(words)
print("count of the words:",count)
file.close()

#reading the content in the file
file=open("student.txt","r")
read=file.read()
print(read)

#implementing ZeroDvisionError in division
try:
 a=int(input())
 b=int(input())
 c=a//b
 print(c)
except ZeroDivisionError:
    print("error") 

#creating a calculator with exception handling
while True:
   try:
      x = int(input("enter the number: "))
      y = int(input("enter the number: "))
      operation = input("enter the operation: ")
      if operation == "+":
         print("addition of two numbers:", x + y)
      elif operation == "-":
         print("subtraction of two numbers:", x - y)
      elif operation == "*":
         print("multiplication of two numbers:", x * y)
      elif operation == "/":
         print("division of two numbers:", x / y)
      else:
         print("invalid operation")
   except (ValueError, ZeroDivisionError) as e:
      print("error:", e)
   
   choice = input("do you want to continue? (yes/no): ")
   if choice!= "yes":
      break   