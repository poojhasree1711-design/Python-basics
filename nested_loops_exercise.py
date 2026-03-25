#nested loop in for loop
for i in range(3): #row
    for j in range(5): #col
        print("SIR",end=" ")
    print()

#nested loop in while condition
i=1
while i<=2:
    j=2
    while j<=2:
        print("sir",end=" ")
        j+=1
    print()
    i+=1

#multiplication table of five
row=5
print("\n-----multiplication table of five------")
for i in range(1): #outer loop runs one time(row)
    for j in range(1,11): #inner loop runs from 1 to 10(column)
          print(row,"x",j,"=",row*j) #it returns the output in the format of table
    print()
