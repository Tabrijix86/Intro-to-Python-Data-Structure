number = 25
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == number:
        print(f"Correct (Guess count {attempts})")
        break
    if guess > number:
        print(f"Too large (Guess count {attempts})")
    else:
        print(f"Too small (Guess count {attempts})")
