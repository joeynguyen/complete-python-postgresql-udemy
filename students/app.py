def create_student(grades):
    user_name = input("What is your name? ")
    return {'name': user_name,
            'grades': grades}

def add_grade(student, grade):
    student['grades'].append(grade)

def calculate_avg_grade(student):
    count = len(student['grades'])
    if count == 0:
        return 0

    total = sum(student['grades'])
    return total / count

new_student1 = create_student([])

new_student1['grades'].append(5)
print(new_student1)

add_grade(new_student1, 90)
print(new_student1)

new_student2 = create_student([80, 70, 60])
new_student3 = create_student([85, 95, 75])
new_student4 = create_student([])
print("new_student2 avg: ", calculate_avg_grade(new_student2))
print("new_student3 avg: ", calculate_avg_grade(new_student3))
print("new_student4 avg: ", calculate_avg_grade(new_student4))
