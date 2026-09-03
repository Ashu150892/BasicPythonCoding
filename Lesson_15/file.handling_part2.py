import os

print(os.getcwd())

if not os.path.exists("Test_Folder"):
    os.mkdir("Test_Folder")
    print("Folder created")
else:
    print("Folder already exists")

items = os.listdir()

print(items)

for item in os.listdir():
    print(item)

import csv
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip header

    for row in reader:
        print("Name:", row[0])
        print("Course:", row[2])

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[2]=="Python":
         print("Name:", row[0])

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Department"])
    writer.writerow(["Ashutosh", 34, "Performance"])
    writer.writerow(["Rahul", 30, "Testing"])
        