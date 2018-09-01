# this construct handles opening and closing the file
with open('my_file.txt', 'w') as f:
    f.write('Hello, world!')

with open('my_file.txt', 'r') as f:
    print(f.readline())
