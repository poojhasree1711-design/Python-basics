#OPERATORS
#arithmetic +,-,**,*,/,//,%
pen=17
pencil=6
print(pen+pencil) #addition
print(pen-pencil) #subtraction
print(pen*pencil) #multiplication
print(pen/pencil) #division
print(pen**pencil) #expoential
print(pen%pencil) #modulo
print(pen//pencil) #floor division(removes decimal)

#relational <=,<,>,>=,==,!=
t=9
u=6
v=9
print(t==v)
print(t==u)
print(t>u)
print(t<v)
print(t!=u)
print(t<=u)
print(v>=u)

#logical
r=56
s=54
print(r<60 and s>40) #true*true=true
print(r>s and s==45) #true*false=false
print(r==56 or s==r) #true+false=true
print(r!=56 or s>60) #false+false=false
print(not True)
print(not(r!=56))

#assignment +=,-=
num1=22
num2=13
num1+=3 #addition
print(num1)
num2-=3 #subtraction
print(num2)
print(num1+num2)

#assignment *=,/=,%=
num3=4.16
num4=3.8
num3*=2 #multiply
num4%=3.80 #modulo
print(num3,num4)

#membership in,not in
member1="PooJHaSree1306"
member2="JH"
print(member2 in member1)
print("sree"in member1)
print("p"not in member1)

#identity is,is not
num5=99
num6=100
print(num5 is num6)
print(num5 is not num6)
if num5 is not num6:
  print(num5)
else:
 print(num6)

#bitwise ~,<<,>>,&,|
n=5
m=6
print(n&m)
print(m|n)
print(n>>1)
print(m&n<<1) #mixed
print(~m)