# person = {
#     "name": "John Doe",
#     "nationality": ["American", "British"],
#     "favourite_programming_language": "Python",
#     "age": 30,
#     "hobbies": ["reading", "traveling", "coding"]
# }

# print(person)

practice_dict = { "London": "England", "Edinburgh": "Scotland", "Cardiff": "Wales", "Belfast": "Northern Ireland" }
print(practice_dict.keys())
print("--------------------------------")
print(practice_dict.values())
print("--------------------------------")
print("The key I want is: " + practice_dict.get("London"))
print("--------------------------------")
print(practice_dict.items())
print("--------------------------------")
print("The pop key is: " + practice_dict.pop("Cardiff"))
print("--------------------------------")
print("The cleared dictionary is: " + str(practice_dict.clear()))
print("--------------------------------")
print("The default key is: " + practice_dict.setdefault("Belfast", "Northern Ireland"))
