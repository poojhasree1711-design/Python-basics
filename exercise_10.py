#printing the day of a given dates
from datetime import datetime
dates=["2026-03-16","2026-03-20"]
days=[]
for d in dates:
    obj=datetime.strptime(d,"%Y-%m-%d")
    days.append(obj.strftime("%A"))
print(days)

#set comprehension--> unique chars phn numbrs which is not used 
phone_number={"9876543220","9967344288","9999555532"}
used_digits={d for num in phone_number for d in num}
all_digits={str(i) for i in range(10)}
unused=all_digits-used_digits
if unused:
    print("unused digits:", unused)
else:
    print("all digits are used")