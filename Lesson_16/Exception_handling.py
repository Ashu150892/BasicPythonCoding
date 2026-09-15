try:
    number = int("abc")
except ValueError as error:
    print("Error:", error)

import json

try:
    with open("employee_90.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    print("JSON file not found")

except json.JSONDecodeError:
    print("Invalid JSON format")


try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program finished")



try:
    number = 10 / 0
    print("Success")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")

finally:
    print("Done")



age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Valid age")

except ValueError as error:
    print("Error:", error)



balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise ValueError("Insufficient balance")

    balance = balance - withdraw
    print("Remaining balance:", balance)

except ValueError as error:
    print("Error:", error)
