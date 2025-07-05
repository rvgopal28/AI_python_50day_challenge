# EvenOddChecker.py

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Part 1: Check a single number
try:
    user_input = int(input("Enter a number to check if it's even or odd: "))
    result = check_even_odd(user_input)
    print(f"{user_input} is {result}.")
except ValueError:
    print("Please enter a valid integer.")

# Part 2: Check a list of numbers
number_list = [10, 15, 22, 33, 42, 55, 60]

print("\nChecking a predefined list of numbers:")
for number in number_list:
    status = check_even_odd(number)
    print(f"{number} is {status}.")
