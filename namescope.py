hero="mike"
def teaser():
    hero="will"
    def trailer():
        hero="eleven"
        print(f"the mage:{hero}")
    trailer()

    print(f"the sorcerer:{hero}")

teaser()
print(f"the paladin:{hero}")

bank="SBI"
def cust_accnt():
    balance=10000
    def deposit():
        nonlocal balance
        amount=5000
        balance+=amount
        print(f"balance after deposit:{amount}")
    deposit()
    print(f"balance after deposit:{balance}")
cust_accnt()  
print(f"bank name:{bank}")  