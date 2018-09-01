class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

def create_student():
    name = input("Enter student name: ")
    return Student(name)

def add_grade(student, grade):
    student.grades.append(grade)

def calculate_avg_grade(student):
    count = len(student.grades)
    if count == 0:
        return 0

    total = sum(student.grades)
    return total / count

def print_student_details(student):
    print("{}, average grade: {}.".format(student.name,
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
            new_student = create_student()
            student_list.append(new_student)
        elif selection == 'a':
            id = int(input("Enter the ID of the student to add a grade to: "))
            grade = int(input("Enter the grade to add: "))
            add_grade(student_list[id], grade)

        selection = input(selection_text)


menu()
