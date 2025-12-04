secret_password = "gizmo"
user_guess = ""
while user_guess != secret_password:
    user_guess = input("Enter Password: ")
    if user_guess != secret_password:
        print("Access Denied")

print("Access Granted")