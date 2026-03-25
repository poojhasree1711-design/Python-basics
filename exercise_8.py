# Store Even Numbers in File
# Ask the user to enter 10 numbers.
# Save only even numbers to a file.
# Example file (even_numbers.txt)
# write function to get the data and storing it
 
# Count Vowels in File
# Write a function that reads a file and counts total vowels.
 
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# Print the statement 

# stores the even number only in a file(even_numbers.txt)
def even():
 with open("even_numbers.txt","w+") as f:
    for i in range(10):
        num=int(input("enter:"))

        if num%2==0:
            f.write(str(num)+"\n")
    data=f.read()

even()

#write and read the count of vowels in a file(vowels.txt)
def vowels():
   with open("vowels.txt","w") as file:
      var=input("enter text:")
      file.write(var)

   with open("vowels.txt","r") as file:
    data=file.read()
    count=0
    for i in data:
        if i.lower() in "aeiou":
            count+=1
    print("count:",count)

vowels()

#printing the pyramid and reverted pyramid
n =5
for i in range(1, n+1): #it represents the top pyramid
#two inner loops, inner loop 1 represents the space and inner loop 2 represents the stars
    for j in range(n-i): #spaces
        print(" ", end="")

    for k in range(2*i-1): #stars
        print("*", end="")

    print()
for i in range(n-1, 0, -1):

    for j in range(n-i): #spaces
        print(" ", end="")

    for k in range(2*i-1):#stars
        print("*", end="")

    print()

