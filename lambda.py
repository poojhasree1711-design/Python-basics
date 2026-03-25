def Calculator(a,b):
    print("addition:",(lambda a,b:a+b)(a,b))
    print("subtraction:",(lambda a,b:a-b)(a,b))
    print("multiplication:",(lambda a,b:a*b)(a,b))
    print("division:",(lambda a,b:a//b)(a,b))
Calculator(15,3) 

num=[1,2,7,5]
result=sorted(num,key= lambda x:x,reverse=True)
print(result)

