
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

def get_highest_grade(grades):
    highest = 0
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest

def get_lowest_grade(grades):
    lowest = 100
    for grade in grades:
        if grade < lowest:
            lowest = grade
    return lowest

def get_n_students_above_passing_grade(grades, passing_grade):
    n_students = 0
    for grade in grades:
        if grade >= passing_grade:
            n_students += 1
    return n_students


print("Welcome to the grade helper!")

n_students = int(input("How many students you have? "))

passing_grade = 6

grades = []

for i in range(n_students):
    grade = int(input("Enter the grade for student no. " + str(i+1) + ": "))
    grades.append(grade)

hline = "-" * 40

print(hline)
print(grades)
print(hline)

print("The average grade is: " + str(calculate_average(grades)))
print("The highest grade is: " + str(get_highest_grade(grades)))
print("The lowest grade is: " + str(get_lowest_grade(grades)))
print("The number of students above passing grade is: " + str(get_n_students_above_passing_grade(grades, passing_grade)))
