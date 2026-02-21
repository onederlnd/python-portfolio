# COMPLETED
import random
def hint(secret_number):
    if secret_number > 50:
        print ("It's above 50!")
    else:
        print ("It's below 50!")

playing = True
while playing:
    print("Welcome!")
    print("RULES: 7 attempts to guess the number. Here's a hint, the number is between 1-100! For another hint, type 'hint' -- without the quotes.")
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    guessed_correctly = False
  
    while not guessed_correctly and attempts < max_attempts:
      
        guess = input()
        if guess == "hint":
            hint(secret_number)
            continue
          
        try:
            guess = int(guess)
        except:
            print("Digits only!") 
            continue
        attempts += 1
        if guess == secret_number:
            print("You guessed it!")
            guessed_correctly = True
        else:
            remaining = max_attempts - attempts
            print(f"Try again! You have {remaining} guesses left!") 
    if not guessed_correctly:
        print("You've lost!")
        answer = input("Play again (Yes or No)? ").lower()
        if answer == "yes":
            playing = True
        else:
            playing = False
