#!/usr/bin/python3
# Password Validation with Retry Alert and Digit Check

correct_password = "Open123"
attempts = 0

while True:
    password = input("Enter password: ")
    attempts += 1

    # Count digits using a for loop
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1

    # Digit validation
    if digit_count == 0:
        print("Error: Need a digit.")
    elif password != correct_password:
        print("Access denied.")
    else:
        print("Access granted.")
        break  # Exit loop if password is correct

    # Retry alert
    if attempts > 2:
        print("Alert: Too many failed attempts.")
