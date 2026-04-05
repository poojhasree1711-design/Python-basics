def largest():
 list=[23,12,78,43]
 largest=list[0] #to store the largest number
 for i in list:
     if(i>largest):
        largest=i #if it satisfies the above condition this input works and continues loop until the list ends
        print("the largest number:",largest)
largest()

def FifthTable():
 n=int(input("range:"))
 for i in range(n):
    i=i*5 #returns the multiplication table five for defined range of input
    print(i)

FifthTable()

def sign(list):
 for i in list:
     print("positive number is:",i) if(i>0)  else print("negative number is",i)
  #returns if the number is positve or negative        
sign([1,-2,+3,4,-99])          
