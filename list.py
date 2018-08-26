numbers = '5,6,8,4'
numbers_array = numbers.split(',')
print('numbers_array', numbers_array)

numbers_array_as_int = []
for number in numbers_array:
    numbers_array_as_int.append(int(number))

print('numbers_array_as_int', numbers_array_as_int)

numbers_array_as_int2 = [int(number) for number in numbers_array]
print('numbers_array_as_int2', numbers_array_as_int2)
