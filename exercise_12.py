#unpacking the tuple and using conditions print the name of student with avg>70

students = [("Arun", 80, 75, 55),("Bala", 85, 90, 50),("Charan", 90, 85, 88),("Divya", 72, 55, 90)]
for name, m1, m2, m3 in students:
    avg = (m1 + m2 + m3)/3
    if avg > 70 and (m1 < 60 or m2 < 60 or m3 < 60):
        print("name:",name,",","avg:", avg)


#Read from input file and write valid numbers to output file

with open("input.txt","w") as file1:
    file1.write("poojha 15 bcd\n")
    file1.write("20 17\n")
    file1.write("18 hope\n")
    file1.write("21.3 netflix\n")            
    file1.write("june 13 2013\n")

with open("input.txt", "r") as file1,open("output.txt", "w") as file2:
    for line in file1:
        items = line.split()  # split words/numbers
        
        for item in items:
            try:
                num = int(item)   # try converting to integer
                file2.write(str(num) + "\n")  #store valid number
            except ValueError:
                print("ValueError")  #ignore invalid data


#recursive function to count the even numbers in a list

def count_even(lst):
    # Base case: empty list
    if not lst:
        return 0
    # Check first element
    if lst[0]%2 == 0:
        return 1+count_even(lst[1:])
    else:
        return count_even(lst[1:])

numbers=[int(i) for i in range(10)]
print(numbers)
print("Number of even numbers:", count_even(numbers))

#getting input in args and finding the product of positive numbers only

def positive_product(*args):
    product=1
    has_positive=False #to handle if it has no positive integers
    for item in args:
        try:
            if int(item)>0: #only positive integers
                product*=int(item)
                has_positive=True
        except (ValueError, TypeError) as e:
            print("error:",e) #ignore invalid inputs
    return "product:",product if has_positive else "has no positive integers"

print(positive_product(2, -3, "5", "abc", 4, 0, 20.3))
print(positive_product(-1, "xyz")) 