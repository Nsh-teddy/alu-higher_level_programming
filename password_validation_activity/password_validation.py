#!/usr/bin/python3

# Experiment 1: Basic Password Check

correct_password = "Open123"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Access denied.")

# Experiment 2: Improved Password Check

correct_password = "Open123"
attempts = 0

while True:
    password = input("Enter password: ")
    attempts += 1

    # Count digits using a for loop (nested inside while)
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1

    if digit_count == 0:
        print("Error: Need a digit.")
    elif password != correct_password:
        print("Access denied.")
    else:
        print("Access granted.")
        break

    if attempts > 2:
        print("Alert: Too many failed attempts.")
