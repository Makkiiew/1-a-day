import random
secret_number = random.randint(1, 100)
user_guess = ""
attempt = 0
while user_guess != secret_number:
    user_guess = int(input("Please Guess the number "))
    attempt += 1
    if user_guess > secret_number:
        print("Incorrect Too High. Try Again!")
    elif user_guess < secret_number:
        print("Incorrect Too Low. Try Again!")
    else:
        attempt += 1
    

print(f"You Win! The number is {secret_number}!")
if attempt > 1:
    print(f"Number of attempts made was {attempt}")
else:
    print(f"WOW!? Just {attempt} Attempt")
