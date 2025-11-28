#Typo Correction from you
username = input('Please enter your name ')
#Updated function that applies int to the input to only allow numbers to be executed
#birth_year = input('Please enter your birth year ')
birth_year = int(input('Please enter your birth year '))
current_year = 2025
#Calculate age based on current year
#birth year been cleaned up removing the int data type
user_age = (current_year - birth_year)
print(f'Hello {username}, you are {user_age} years old today.')