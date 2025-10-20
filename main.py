import random

secret_number = random.randint(1,10)

while True:
    guess = int(input("Enter guess number: "))
    if guess == secret_number:
        print("Topdingiz 🎉")
        break
    else:
        print("Topolmadingiz ❌")
