# Secure Sample Application

username = input("Enter username: ")

if username.strip() == "":
    print("Username cannot be empty.")
else:
    print("Login request received for:", username)
    print("Password is not displayed for security.")