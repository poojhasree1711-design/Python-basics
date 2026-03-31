#"1":
# Task Name: Library Book Manager
# Instructions:
# Base Class: Create a class named Book.
# Use __init__ to take title and author.
# Create a Private Attribute named __price (use double underscores). Set a default value like 500.
# Encapsulation: In the Book class, create a method named show_details().
# It should print the Title and Author.
# It should NOT print the price directly. Create a separate method get_price() to return the price only when called.
# Inheritance: Create a child class named EBook that inherits from Book.
# Add a new attribute called file_size (e.g., "2MB").
# Override the show_details() method to print the Title, Author, AND the File Size.
# Polymorphism: Create another child class named Paperback.
# Override the show_details() method to print the Title and Author, plus a message: "This is a physical copy."
# Execution:
# Create an object for EBook and an object for Paperback.
# Store them in a list and run a loop to call show_details().
# Try to print print(my_book.__price) and see if it gives an error!

#Base case
class Book:
    def __init__(self, title, author, price=500):
        self.title = title
        self.author = author
        self.__price = price #private

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price>0:
            self.__price = new_price
        else:
            print("Invalid price!")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def show_details(self):
        super().show_details()
        print(f"File Size: {self.file_size}")

class Paperback(Book):
    def show_details(self):
        super().show_details()
        print("This is a physical copy.")

#Example case
ebook=EBook("Atomic Habits", "James Clear", "5MB")
paper=Paperback("Deep Work", "Cal Newport")
books=[ebook, paper]

for book in books:
    print("\n---")
    book.show_details()

# Encapsulation test
print("\nPrice:",ebook.get_price())

#Changing price
ebook.set_price(750)
print("Updated Price:",ebook.get_price())


#"2":
# Task Name: Email Processing System
# Instructions:
# Base Class: Create a class named Email. Use the __init__ method to initialize an attribute called address (the email ID).
# Inheritance: Create a child class named EmailSlicer that inherits from the Email class.
# Define a method named process() inside this class.
# This method should split the email using the @ symbol and print the Username and Domain separately.
# (Example: "student@gmail.com" -> Username: student, Domain: gmail.com)
# Polymorphism: Create another child class named EmailValidator that also inherits from Email.
# Define a method named process() (use the exact same name).
# This method should check if both @ and . symbols exist in the email and print whether the email is "Valid" or "Invalid."
# Execution:
# Create a list containing objects of both EmailSlicer and EmailValidator.
# Use a for loop to call the process() method for each object and observe how the same method name performs different actions!

#Base Class
class Email:
    def __init__(self, address):
        self.address=address

#Child Class-EmailSlicer
class EmailSlicer(Email):
    def process(self):
        if "@" in self.address:
            username, domain=self.address.split("@")
            print(f"Username: {username}")
            print(f"Domain: {domain}")
        else:
            print("Invalid format for slicing")

#Child Class-EmailValidator
class EmailValidator(Email):
    def process(self):
        if"@"in self.address and"."in self.address:
            print(f"{self.address}-->Valid Email")
        else:
            print(f"{self.address}-->Invalid Email")

#Execution
emails = [
    EmailSlicer("student@gmail.com"),
    EmailValidator("student@gmail.com"),
    EmailSlicer("wrongemail.com"),
    EmailValidator("hello@com")]

for obj in emails:
    print("\n--- Processing ---")
    obj.process()