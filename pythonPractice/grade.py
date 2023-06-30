m = int(input('Enter total marks for CSE203 (out of 100): '))
if 90 <= m <= 100:
    grade = 'A'
elif 85 <= m <= 89:
    grade = 'A-'
elif 80 <= m <= 84:
    grade = 'B+'
elif 75 <= m <= 79:
    grade = 'B'
elif 70 <= m <= 74:
    grade = 'B-'
elif 65 <= m <= 69:
    grade = 'C+'
elif 60 <= m <= 64:
    grade = 'C'
elif 55 <= m <= 59:
    grade = 'C-'
elif 50 <= m <= 54:
    grade = 'D+'
elif 45 <= m <= 49:
    grade = 'D'
else:
    grade = 'F'
print('Grade is:', grade)
