# FOR LOOP APPROACH

passwords = [
    {"service": "acebook", "password": "password123", "added_on": "21/03/22"},
    {"service": "gmail", "password": "qwerty123", "added_on": "21/03/22"},
    {"service": "makersbnb", "password": "qwerty789", "added_on": "22/03/22"}
]

def any_passwords_added_on_21_03_22(passwords):
    for password in passwords:
        if password["added_on"] == "21/03/22":
            return True
    return False

print(any_passwords_added_on_21_03_22(passwords))
# True

# ---------------------------------

# LAMBDA APPROACH

passwords = [
    {"service": "acebook", "password": "password123", "added_on": "21/03/22"},
    {"service": "gmail", "password": "qwerty123", "added_on": "21/03/22"},
    {"service": "makersbnb", "password": "qwerty789", "added_on": "22/03/22"}
]

any_passwords_added_on_21_03_22 = lambda passwords: any(password["added_on"] == "21/03/22" for password in passwords) # For each password record, check whether its added_on date is 21/03/22

print("Are there any passwords added on 21/03/22?", any_passwords_added_on_21_03_22(passwords))
# True

# ---------------------------------

# a function that returns a list of all passwords added on 22/03/22

passwords = [
    {"service": "acebook", "password": "password123", "added_on": "21/03/22"},
    {"service": "gmail", "password": "qwerty123", "added_on": "21/03/22"},
    {"service": "makersbnb", "password": "password?!776", "added_on": "22/03/22"},
    {"service": "twitter", "password": "qwerty4%56", "added_on": "22/03/22"}
]

passwords_added_on_22_03_22 = lambda passwords: [password for password in passwords if password["added_on"] == "22/03/22"]

print("Passwords added on 22/03/22:", '\n' + str(passwords_added_on_22_03_22(passwords)))

# ---------------------------------

(print("Using a for loop to double each number in a list"))
(print("---------------------"))

numbers = [1, 2, 3, 4]

result = []

for number in numbers:
    result.append(number * 2)

print("Result using for loop:", result)