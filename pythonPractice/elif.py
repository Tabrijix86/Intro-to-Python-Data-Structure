marks = input("Please enter your marks: ")
marks = float(marks)

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "A-"
elif marks >= 60:
    grade = "B+"
elif marks >= 50:
    grade = "B-"
elif marks >= 30:
    grade = "C+"
elif marks >= 20:
    grade = "C-"
else:
    grade = "F"
print("Your grade is: ", grade)
