def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(5, 3))

def add_three_numbers(num1, num2, num3):
    return num1 + num2 + num3

print(add_three_numbers(5, 3, 2))

def concatenate_friends_names(name1, name2):
    return name1 + " and " + name2

print(concatenate_friends_names("Andy", "Min"))

def calculate_number_of_seconds_in_x_weeks(weeks):
    return weeks * 7 * 24 * 60 * 60

print(calculate_number_of_seconds_in_x_weeks(3))

# Output:

# ➜  code-practice git:(main) ✗ python3 first-functions.py
# 8
# 10
# Andy and Min
# 1814400