def create_student(name, grades):
    if name == '':
        user_name = input("Enter student name: ")
    else:
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


def print_student_details(student):
    print("{}, average grade: {}.".format(student['name'],
                                          calculate_avg_grade(student)
                                         )
         )

def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: ", i)
        print_student_details(student)

student_list = []
selection_text = """
    Enter 'p' to print the student list,
    's' to add a new student,
    'a' to add a grade to a student,
    or 'q' to quit.
    Enter your selection: """

def menu():
    selection = input(selection_text)
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            new_student = create_student('', [])
            student_list.append(new_student)
        elif selection == 'a':
            id = int(input("Enter the ID of the student to add a grade to: "))
            grade = int(input("Enter the grade to add: "))
            add_grade(student_list[id], grade)

        selection = input(selection_text)


menu()
