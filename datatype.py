#finding type
x=1
c=5+7j
d=45.677
e= True
print(type(x))
print(type(c))
print(type(d))
print(type(e))


#int to float,complex
y=56
z=float(y)
a=complex(z)
print(z,a)

#float to int,complex
b=5.453
print(int(b))
print(complex(b))
print(bool(b))

#complex to int, float
g=5+6j
f=int(g.imag)
h=int(g.real)
print(f,h)
yy=float(g.imag)
hh=float(g.real)
print(yy,hh)

#bool to int,float,complex
hg= True 
gh= False
print(int(hg),int(gh))
print(float(hg),float(gh))
print(complex(gh),complex(hg))


#immutability
#string
st="make" #cant change
result=(st.replace("m","b")) #can replace
print(result)

#bool
b1= True
b1= False
print(bool)#created a new one

#int
x=5
print(id(x)) #old one
x=x+5
print(id(x)) #new one

#float
u=3.1
print(id(u))
u=u+0.4
print(u)
print(id(u))

#complex
co=3-4j
print(co.real,co.imag, id(co))
co=co+9j
print((co),id(co))


#mutable
#list
list=[1,2,3,4]
print(id(list)) 
list[2]=6
print(list)
print(id(list)) 


p=input()
print(p+10)
