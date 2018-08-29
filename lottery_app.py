import random

# User can pick 6 numbers
def get_player_numbers():
    numbers_csv = input("Enter your 6 unique numbers between 1 and 20, separated by commas: ")
    # Now I want to create a set of integers from this numbers_csv
    numbers_list= numbers_csv.split(',')
    numbers_set = {int(number) for number in numbers_list}
    return numbers_set

player_numbers = get_player_numbers()
print('player_numbers', player_numbers)

# Lottery calculates 6 random numbers (between 1 and 20)
def get_lottery_numbers():
    lottery_numbers = set()
    while len(lottery_numbers) < 6:
        lottery_numbers.add(random.randint(1,20))
    return lottery_numbers

lottery_numbers = get_lottery_numbers()
print('lottery_numbers', lottery_numbers)

# Then we match the user numbers to the lottery numbers
# Calculate winnings based on how many numbers the user matched
def calculate_winnings(player_nums, lottery_nums):
    matched_nums = lottery_nums.intersection(player_nums)
    return "You matched {}. You won ${}.".format(matched_nums, len(matched_nums) ** 5)

lottery_results = calculate_winnings(player_numbers, lottery_numbers)
print('lottery_results', lottery_results)
