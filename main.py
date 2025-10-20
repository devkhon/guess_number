import random

secret_number = random.randint(1,10)

count = 0

while count<3:
    guess = int(input("Enter guess number: "))
    if guess == secret_number:
        print("Topdingiz 🎉")
        break
    else:
        print(f"Topolmadingiz ❌>> {count}")
    count = count + 1
    
