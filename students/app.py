def create_student(name, grades):
    user_name = name
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

new_student1 = create_student('Tim', [])

new_student1['grades'].append(5)
print(new_student1)

add_grade(new_student1, 90)
print(new_student1)

new_student2 = create_student('Joe', [80, 70, 60])
new_student3 = create_student('Bill', [85, 95, 75])
new_student4 = create_student('Bob', [])

student_list = []
student_list.extend([new_student1, new_student2, new_student3, new_student4])
print(student_list)

def print_student_details(student):
    print("{}, average grade: {}.".format(student['name'],
                                          calculate_avg_grade(student)
                                         )
         )

for student in student_list:
    print_student_details(student)
