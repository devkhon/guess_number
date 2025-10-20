import random

secret_number = random.randint(1,10)

guess = int(input("Enter guess number: "))

if guess == secret_number:
    print("Topdingiz 🎉")
else:
    print("Topolmadingiz ❌")
