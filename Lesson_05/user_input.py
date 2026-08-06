name = input("Enter your name :")
pin = input("Enter you pin")

print(type(str(20)))
print(type(int(20)))
print(type(int("20")))

print(type(name))
print(type(pin))

print(" ====== My Profile =======")
name = input("Enter Name :")
age = int(input("Enter Age :"))
city = input("Enter City :")
print(name)
print(age)
print(city)
print(type(name))
print(type(age))
print(type(city))

print(" Ask user to enter 2 number:")

num_1 = int(input("Enter First Number"))
num_2 = int(input("Enter Second Number"))

print("Sum :", num_1+num_2)
print("Sub :", num_1-num_2)
print("Multiple :", num_1*num_2)
print("Divide :", num_1/num_2)


print("Area of Rectange: ")
length = int(input("Enter the length: "))
width = int(input("Enter the width"))

area = length*width
print("Area :", area)

print(" Calculate Student Percentage :")
marks_english= float(input("Enter English marks"))
marks_maths= float(input("Enter Maths marks"))
marks_science= float(input("Enter Science marks"))

total_marks = marks_english+marks_maths+marks_science
print("Total Marks :", total_marks)
avg_marks =total_marks/3
print("Average :", avg_marks)
percent = ((total_marks)/300)*100
print("Student Percentage :", percent)