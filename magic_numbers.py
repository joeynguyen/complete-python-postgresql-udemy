numbers = [0, 1, 2 ,3, 4]
print('numbers:', numbers)
print('numbers length:', len(numbers))
print('last number:', numbers[len(numbers) - 1])

for number in numbers:
    print('{} to the power of 2 = {}'.format(str(number), str(number ** 2)))

magic_numbers = [3, 5, 9]
chances = 3
guess_correct = False

for attempt in range(chances): # range(chances) is [0, 1, 2]
    user_number = input('Enter a number between 0 and 9: ')
    print('This is attempt #{}'.format(attempt + 1))
    if int(user_number) in magic_numbers:
        print("You guessed right!")
    else:
        print('You guessed wrong')
        chances = chances - 1
