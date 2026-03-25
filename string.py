#STRING is immutable,indexed,ordered and can aloows dupes

#cases
s="poojha SREE1711"
print(s.upper())
#returns the value in uppercase
print(s.lower())
#returns the value in lowercase
print(s.title())
#retunrs capitalise of the string
print(s.capitalize())
#returns the first lettter in capital
print(s.casefold())
#more stronger than lower()

print(s.replace("jh","JH"))
#replace the particular part with given one
print(s.swapcase())
#swaps the case
print(len(s)) 
#length of the string

#isaplha,isdigit,isalnum,islower,isupper,isascii(returns true or false)
print(s.isalpha())
print(s.isalnum())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print("aeiou".isascii())
#to find if the string is ascii or not
print("co℅".isascii())
#unicode symbols will return false

print(s.find("5")) #find the index of the value
print(s.index("1")) #index of the value
print(s.rindex("1")) #returns index value from right

#endswith,startswith
print(s.endswith("11"))
print(s.startswith("p"))

print(s.count("1")) #count the value how many times apperared

#stripping
print("   python,   yh  ".lstrip(" ")) #strips from left
print("   friend   ".rstrip(" ")) #strips frim right

#indexing,slicing
print(s[1])
print(s[3:5]) #slicing

print(f"I'm {s}") #formatting
print(s.encode()) #encoding

#membership
print("SREE"in s)
print("P"not in s)


#join,split
string2="hi   how are  you"
print((string2.split()))
#returns the list of the string
print(" ".join(string2))
#returns the list to string
print("-".join(string2.split()))
#returns the string converted into list and joined by hyphens

#maketrans,translate
string3="p"
print(ord(string3))
print(ord("Z"))
#returns the character to number

string4=94
print(chr(string4))
print(chr(77))
#returns the number to character

string5="bicycle"
print(ord(string5[3]))
#returns the number of particular index value
table=string5.maketrans("iepc","5182")
#makes the table to translate
print(string5.translate(table))
#returns the translated table


#partition,rpartition
string6="123*6=7ac=df"
print(string6.partition("3"))
#returns the parted into three parts (before,parted one,after)
print(string6.partition("=7"))
#partition from left occurence of tbe string
print(string6.rpartition("="))
#partition from right side of the string

#expandtabs
string7="cow\tanimal\tcalf"
print(string7.expandtabs(11).expandtabs(5))
#returns the space we desired between the values where ever "\t" is placed
