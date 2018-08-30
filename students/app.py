def create_student():
    user_name = input("What is your name? ")
    return {'name': user_name,
            'grades': []}

def add_grade(student, grade):
    student['grades'].append(grade)

new_student = create_student()

new_student['grades'].append(5)
print(new_student)

add_grade(new_student, 90)
print(new_student)

