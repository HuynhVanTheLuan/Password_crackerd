from time import time

password = input("Enter Password: ")
start = time()
letters = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
special = "!@#$%^&*()_+-=|;':,./<>?`~"
chars = letters + number + special

guess = []
for val in range(12):
    a = [i for i in chars]
    for y in range(val):
        a = [x + i for i in chars for x in a]
        guess = guess + a
        if password in guess:
            break

print(f"{password=} : {len(guess)} guesses")
print(f"Runtime: {str(time()- start)}")
