#greatest of two numbers
p=23
q=47
if(q<p):
 print("the greatest number is",p)
else:
 print("the greatest number is:",q)


#age elgibility for discount
hope=10
if(hope<12):
    print("eligible")
else:
    print("not eligible")

#looping pgm for string
str="whEEler"
result=""
for i in str:
  if(i.isupper()):
    result+=i.lower()
  else:
    result+=i.upper()
  print(result)

#join
name=["mike","will"]
print("~".join(name))

#join+split
st="mike   wheeler and will byers"
print("-".join(st.split()))
print(" ".join(st.upper().split()))

name=input()
score=int(input())
department=input()
print("my name is",name)
print("my score is",score/10)
print("my department is", department)

meghna=input()
if(meghna=="died"):
    print("surya meets priya")
else: 
    print("surya weds meghna")   

mark=int(input())
if(mark>35):
    print("pass")
else:
    print("fail")

income=int(input("income:"))
if(income>=7000):
    print("scholarship is available")
else:
    print("not available")

num=int(input())
if (num%3==0 and num%5==0):
     print("it is divisble by both 3 and 5")
else:
    print("not divisble by 3 and 5")     

#ternary way
print("divisble") if (num%3==0 and num%5==0) else print("not divisble")  

value=int(input())
if(value%2==0):
    print("it is even")
else:
    print("it is odd")   

mark=int(input())
if(mark<35):
    print("poor student")
elif(35<mark<70):
    print("avg student")
elif(70<mark<100):
    print("good student")
else:
    print("invalid input")         

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
for i in range(0,11):
    if i==5:
        continue
    if i==9:
        break
    print(i)

for b in range(0,21):
    if b%3==0:
        continue
    if b%11==0:
        break
    print(b)

for c in range(0,16):
    if c==13:
        break
    if c%2==0:
        print("Even")
    else:
        print("Odd")
           

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

