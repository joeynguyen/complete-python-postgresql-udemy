sample_dict = {'name': 'Jose',
               'score': [25, 50, 73, 98],
               'exams': {
                   'final': 80,
                   'midterm': 92
               }}

print('name:', sample_dict['name'])
print('score:', sample_dict['score'][3])
print('score:', sample_dict['exams']['midterm'])

def create_user():
    user_name = input("What is your name? ")
    user_age = input("What is your age? ")
    return {'name': user_name,
            'age': user_age}

user_object = create_user()
print("Your name is {} and you are {} years old.".format(user_object['name'], user_object['age']))
