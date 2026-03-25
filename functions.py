
def addition(a,b):#defining the function with def keyword
    print(a+b)

addition(3,4)#calling the function by calling the function_name        

#finding a number is odd or even using a function
def number(a):
    return a%2==0 #just return true or false implied by the condition
print(number(13))

#finding the number is odd or even using conditions in a function
def numbers(b):
    if(b%2==0):
        return "even"
    else:
        return "odd"
#in here, having conditions inside the function decides what to return while checking the conditions
print(numbers(12))    

def number(a):
    if a%2==0:
        print("even")
    else:
        print("odd")

x=number(8)

