#"EXPENSES TRACKER management system"

expenses=[]

#get_expenses() function:-
def get_expenses(expenses):
    while True:
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date: ")
        expense={
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
        }
        expenses.append(expense)
        choice=(input("do want to continue(y/n):"))   
        if choice.lower()=="n":
           break       


#view_expenses() function:-
def view_expenses(expenses):
    print("\nTOTAL EXPENSES")
    for e in expenses:
        print("Amount:", e["amount"])
        print("Category:", e["category"])
        print("Description:", e["description"])
        print("Date:", e["date"])
        print()


#total_expenses() function:-
def total_expenses(expenses):
    total=0
    for i in expenses:
        total=total+i["amount"]
    print("total amount spent:",total)


#main() function:-
def main():
    while True:
        print("1.get the expenses")
        print("2.view the expenses")
        print("3.total amount spent")
        print("4.exit")
        choice=int(input("enter the choice:"))
        if choice==1:
            get_expenses(expenses)
        elif choice==2:
            view_expenses(expenses)
        elif choice==3:
            total_expenses(expenses)
        elif choice==4:
            print("exited the expenses tracker!")
            break

main()