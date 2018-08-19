# age = 5
age = input('Enter your age: ')
print('You are ' + age + ' years old')
ageInDays = int(age) * 365
print('You are ' + str(ageInDays) + ' days old')
# format method implicitly converts number to string
print('You are {} days old! This is equivalent to {} years.'.format(ageInDays, age))