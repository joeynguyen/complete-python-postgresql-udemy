numbers = [0, 1, 2 ,3, 4]
print('numbers:', numbers)
print('numbers length:', len(numbers))
print('last number:', numbers[len(numbers) - 1])

for number in numbers:
    print('{} to the power of 2 = {}'.format(str(number), str(number ** 2)))