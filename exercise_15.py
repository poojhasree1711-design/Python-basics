# Matrix Multiplication
# Concepts: Nested loops
# Task:
# Multiply two matrices

A=[[1, 2],[3, 4]]

B=[[5, 6],[7, 8]]

result=[[0, 0],[0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j]+=A[i][k]*B[k][j]

for row in result:
    print(row)


# Anagram Checker (Optimized) 
# Concepts: Strings, dictionaries
# Task: 
# Check if two strings are anagrams
# Ignore spaces, case
# Example: 
# listen, silent → True
# Upgrade:
# Handle large inputs efficiently

def is_anagram(s1,s2):
    # remove spaces and convert to lowercase
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    # quick check to handle large input efficiently
    if len(s1)!=len(s2):
        return False

    count={}

    #count characters from first string
    for ch in s1:
        count[ch]=count.get(ch,0)+1

    #subtract using second string
    for ch in s2:
        if ch not in count:
            return False
        count[ch]-=1
        if count[ch]<0:
            return False
    return True

#Example case
print(is_anagram("listen", "silent"))  #True


# File Word Counter
# Concepts: File handling
# Task:
# Read a .txt file
# Count
# words
# lines
# most frequent word

from collections import Counter
#open file
with open("input.txt", "r") as file: #here, I used existing file
    text=file.read()

#count lines
lines=text.split("\n")
line_count=len(lines)

#split words
words=text.lower().split()
word_count=len(words)

#most frequent word
freq = Counter(words)
most_common_word, count=freq.most_common(1)[0]

#output
print("Lines:",line_count)
print("Words:",word_count)
print("Most Frequent Word:",most_common_word)


#Student Management System (CLI)
# Concepts: OOP, lists, dictionaries
# Task:
# Add student
# Remove student
# Show marks
# Calculate average

class StudentSystem:
    def __init__(self):
        self.students={}

    def add_student(self, name):
        if name not in self.students:
            self.students[name]={}
            print("Student added!")
        else:
            print("Student already exists!")

    def add_marks(self,name,subject,marks):
        if name in self.students:
            self.students[name][subject]=marks
            print("Marks added!")
        else:
            print("Student not found!")

    def remove_student(self,name):
        if name in self.students:
            del self.students[name]
            print("Student removed!")
        else:
            print("Student not found!")

    def show_students(self):
        if not self.students:
            print("No students available")
            return
        
        for name, subjects in self.students.items():
            print("Name:",name)
            for sub, mark in subjects.items():
                print(" ",sub,":",mark)

    def average_marks(self,name):
        if name in self.students and self.students[name]:
            marks=self.students[name].values()
            avg=sum(marks)/len(marks)
            print("Average for",name,":",avg)
        else:
            print("No data found!")

#MAIN MENU
def main():
    system=StudentSystem()

    while True:
        print("1. Add Student")
        print("2. Add Marks")
        print("3. Remove Student")
        print("4. Show Students")
        print("5. Average Marks (per student)")
        print("6. Exit")

        choice=input("Enter choice: ")

        if choice=="1":
            name=input("Enter name: ")
            system.add_student(name)

        elif choice=="2":
            name=input("Enter name: ")
            subject=input("Enter subject: ")
            marks=int(input("Enter marks: "))
            system.add_marks(name, subject, marks)

        elif choice=="3":
            name=input("Enter name: ")
            system.remove_student(name)

        elif choice=="4":
            system.show_students()

        elif choice=="5":
            name=input("Enter name: ")
            system.average_marks(name)

        elif choice=="6":
            print("Exited the Student System")
            break

        else:
            print("Invalid choice!")

main()