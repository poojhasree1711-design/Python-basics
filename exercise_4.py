def recursive_sum(n):
    if n==1:
        return 1 #base case 1=1
    else:
        return n+recursive_sum(n-1) #returns the sum of digits in the given range
        #recursive case    
print(recursive_sum(5)) 



def reverse_strings(s,):
    if s=="":
        return "stop" #base case
    else:
        return ("".join(reversed(s[1:])))+s[0] #recursive case
    #here, string can't reverse without loops or slicing because string is immutable so we converted it into list to reverse it.
print(reverse_strings("python"))    

def count_digits(num):
    num=12345
    