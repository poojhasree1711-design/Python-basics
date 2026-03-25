#packing and unpacking:-

#packing the dictionary into key,value pairs(items)
def dict(**args):
    print(*args.items())

dict(name="poojha",age=18,dept="IT")    

#packing a single variable into list
def list(*args):
    print(*args)

list([1,2,3])    