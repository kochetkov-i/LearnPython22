import random


int_numbers = random.sample(range(0,99), 10)

for number in int_numbers:
    print(number +1)

try:
    user_string = str(input("Input string: "))
except ValueError: print("You have mistake in input")
except TypeError: print("You have mistake in input")

for char in user_string:
    print(char)