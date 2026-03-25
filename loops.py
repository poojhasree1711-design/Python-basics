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