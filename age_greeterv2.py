#Typo Correction from you
username = input('Please enter your name ')

#Updated function that applies int to the input to only allow numbers to be executed
#birth_year = input('Please enter your birth year ')
birth_year = int(input('Please enter your birth year '))

current_year = 2025

#Calculate age based on current year
#birth year been cleaned up removing the int data type
user_age = (current_year - birth_year)

#Updated display for information, Depending on age over or under 18
if user_age < 18:
    print(f"Wow {username} only {user_age}, still such a young soul. You must have loads of energy!")
else:
    print(f"{username} you may not be young anymore but at {user_age} you certainly have wisdom!")

