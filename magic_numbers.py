import random

numbers = [0, 1, 2 ,3, 4]
print('numbers:', numbers)
print('numbers length:', len(numbers))
print('last number:', numbers[len(numbers) - 1])

for number in numbers:
    print('{} to the power of 2 = {}'.format(str(number), str(number ** 2)))

magic_numbers = [
    random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9)
]
chances = 3
guess_correct = False

while chances > 0 and guess_correct == False:
    user_number = input('Enter a number between 0 and 9: ')
    if int(user_number) in magic_numbers:
        print("You guessed right!")
        guess_correct = True
    else:
        print('You guessed wrong')
        chances -= 1
        print('You have {} chances left'.format(chances))

minimum = 100
for index in range(10):
    random_number = random.randint(0, 100)
    print('current number is {}'.format(random_number))
    if random_number < minimum:
        minimum = random_number

print('minimum is {}'.format(minimum))
