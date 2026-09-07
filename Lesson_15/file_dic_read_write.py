import csv

with open("employees.csv", "w", newline="") as file:

    fieldnames = ["Name", "Age", "Department"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "Name": "Ashutosh",
        "Age": 34,
        "Department": "Performance"
    })

    writer.writerow({
        "Name": "Rahul",
        "Age": 30,
        "Department": "Testing"
    })



import json

with open("employee.json","r") as file_json:
    read= json.load(file_json)
    
print("Before Update",read)
read["skills"] ="ML"    # Add New
print("After Update",read)
# read["Sex"] ="Male"
# read.pop("skills")[2] = "ML"
print("After Delete",read)
with open("employee.json", "w") as file_json:
    json.dump(read, file_json, indent=4)