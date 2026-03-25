#PROGRAM TO COUNT THE NUMBER OF INTEGERS AND STRINGS IN A LIST
list=[1,"child",78,"boy",54,"girl",3]

def count_types(list):
  count_int=0
  count_string=0
  for i in list:
    if type(i)==int:
        count_int+=1#it is used to count the number of integers in the list and it is incremented by 1 each time
    elif type(i)==str:
        count_string+=1#it is used to count the number of strings in the list and it is incremented by 1 each time
  print(count_int,count_string)

print(count_types(list))

#PROGRAM TO COUNT THE NUMBER OF TIMES EACH ITEM SOLD IN A DAY AND ALSO REMOVING DUPES USING SET
list=["apple","banana","orange","banana","apple"]
print(list) #it returns the items sold overall in a day including the dupes presented there
dict={}
for i in list:
  if i in dict:
    dict[i]+=1
  else:
    dict[i]=1
print(dict)

list=set(["apple","banana","orange","banana","apple"]) #here we are converting the type list[] into set{}, so it remove dupes
print(list)

#CALCULATOR PROGRAM TO PERFROM OPERATIONS INSIDE A FUNCTION AND TO CONTINUE THE CALCULATIONS BY WHILE LOOP
def Calculator(a,b):#defining the function with two parameters
     def Add():
         return a+b
     def Sub():
         return a-b
     def Mul():
         return a*b
     def Div():
         return a/b
     
     print("addition:",Add())
     print("subtraction:",Sub())
     print("multiplication:",Mul())
     print("division:",Div())
     

while True:#to create the loop to continue until the user wants to stop     
 Calculator(5,3)#calling the function 
 choice=input("do you want to continue?")
 if choice=="n":
     break
 else:
    continue   
