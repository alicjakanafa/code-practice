num = 51
if num > 50:
    if num % 2 == 0:
        print(f"{num} is greater than 50 and even")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3 and larger than 50")
    else:
        print(f"{num} is less than or equal to 50 and not divisible by 3")
else:
    print(f"{num} is too small!")