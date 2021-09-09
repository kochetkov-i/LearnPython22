import random


int_counts = random.sample(range(0,99),10)

for count in int_counts:
    print(count +1)

user_string = str(input("Input string: "))

for char in user_string:
    print(char)