# User can pick 6 numbers
# Lottery calculates 6 random numbers (between 1 and 20)
# Then we match the user numbers to the lottery numbers
# Calculate winnings based on how many numbers the user matched

def get_player_numbers():
    numbers_csv = input("Enter your 6 numbers, separated by commas: ")
    # Now I want to create a set of integers from this numbers_csv
    numbers_list= numbers_csv.split(',')
    numbers_set = {int(number) for number in numbers_list}
    return numbers_set

print(get_player_numbers())
