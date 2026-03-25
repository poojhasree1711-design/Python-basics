
class MarksOutOfRange(Exception):
    pass

#function_1:get_marks()
def get_marks():
    marks = []
    
    for i in range(5):
        while True:
            try:
                mark = int(input("Enter mark for subject " + str(i+1) + ": "))
                
                if mark < 0 or mark > 100:
                    raise MarksOutOfRange
                
                marks.append(mark)
                break
                
            except ValueError:
                print("Enter numbers only!")
            except MarksOutOfRange:
                print("Marks must be between 0 and 100")
    
    return marks

#function_2:calculate_average(mark)
def calculate_average(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg


#function_3:assign_grade(avg)
def assign_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 50:
        return "B"
    else:
        return "Fail"

#display_result(total,avg,grade)
def display_result(total, avg, grade):
    print("\nResult")
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)

marks = get_marks()
print("Marks entered:", marks)
total, avg = calculate_average(marks)
grade = assign_grade(avg)
display_result(total, avg, grade)