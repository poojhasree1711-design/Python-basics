# s="mike wheeler loves will byers"
# print(s.count("i"))
# print(s.count("e",0,10))
# print(s[:12].count("e"))
# print(s.count("e",5))  
# print(s.endswith("byers"))
# print(s.index("w",10,20)) 
# print(s.replace("will","cleric"))
# print(s.find("w",3,4))
# print(len(s[3:14]),s)
# print("h".join(s.strip("e"))) #

# string4=94
# print(chr(string4))
# print(chr(94))
# #returns the number to character

# string2="hi   how are  you"
# print((string2.split()))
# #returns the list of the string
# print(" ".join(string2))
# #returns the list to string
# print("-".join(string2.split()))
# #returns the string converted into list and joined by hyphens

# text = "apple,banana,grape,orange"
# print(text.split(","))

# words = ["Python", "is", "awesome"]
# print(" ".join(words))

# text1 = "  I    love    Python   "
# print(" ".join(text1.split()))

# text2 = "  apple, banana , mango ,  orange  "
# print(text2.replace(","," ").split( ))

# text3 = "Python is powerful"
# print(" ".join(reversed(text3.split( ))))


# text4 = "   Python   is   very   powerful   "
# print(len((text4).split()))

# text5 = "###Welcome###"
# print(text5.lstrip("#").rstrip("#"))

# text6 = "  Learn Python The Smart Way  "
# print("-".join(text6.lower().split()))

# email = "student123@gmail.com"
# print(email.split("@")[1])
# print(email)

# text7 = "   python    is   FUN  "
# print(" ".join(text7.title().split()))

# text9= "  apple, banana , mango ,  orange  "
# word=text9.strip().split(",")
# print(word)

# text8 = "  apple, banana , mango ,  orange  "
# wordsa = [w.strip() for w in text8.strip().split(",")]

# num=int(input("enter the number:"))
# if (num%3==0):
#      print("Fizz")
# if(num%5==0):
#      print("Buzz")
# if(num%3==0 and num%5==0):
#      print("FizzBuzz")          
# else:
#     print("no FizzBuzz")     

# str="12345"
# reverse=(str)
# print(reverse)


# def sign(list):
#  for i in list:
#      if(i>0):
#           print("+")
#      else:
#           print("-")

# sign([1,-2,3])          

# def recursive_sum(n):
#     if n==1:
#         return 1 #base case 1=1
#     else:
#         return n+recursive_sum(n-1) #returns the sum of digits in the given range
#         #recursive case    
# print(recursive_sum(5)) 

# def reverse_strings(s,):
#     if s=="":
#         return "stop" #base case
#     else:
#         return ("".join(reversed(s[1:])))+s[0] #recursive case
#     #here, string can't reverse without loops or slicing 
#     #because it is immutable so we converted it into list to reverse it
# print(reverse_strings("python"))    

# def count_digits(n):
#     if n==0:
#         return "stop"
#     else:
#         return n//10 
    
# print(count_digits(12345))    

# def list(args):
#     print(args)

# list([1,2,3])   


# dict_data --> json file(dumps/dump) --> dict_save(load/loads) -> picke(dict_pickle.pxl) -> read(dict_pickle) -> print
 

import datetime
datetime.datetime.now()-datetime.datetime.now().min

#list,set,dict comp--> unique chars phn numbrs not used 
from datetime import datetime
dates=["2026-03-16","2026-03-20"]
days=[]
for d in dates:
    obj=datetime.strptime(d,"%Y-%m-%d")
    days.append(obj.strftime("%A"))
print(days)


phone_number={"9876543220","9967344288","9999555532"}
used_digits={d for num in phone_number for d in num}
all_digits={str(i) for i in range(10)}
unused=all_digits-used_digits
if unused:
    print("unused digits:", unused)
else:
    print("all digits are used")