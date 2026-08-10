num_1 = int(input("Enter the Number :"))
def calculate_square():
    return num_1*num_1
def calculate_cube():
    return num_1*num_1*num_1
square_result=calculate_square()
print(square_result)
cube_result=calculate_cube()
print(cube_result)

num = int(input("Enter the Number :"))
def calculate_square(num):
    return num*num

square_result =calculate_square(num)
print(square_result)

def calculate_cube(square_result):
     return square_result*num
cube_result = calculate_cube(square_result)
print(cube_result)

def calculate_avg():
    return (square_result+cube_result)/2
avg_result=calculate_avg()
print(avg_result)
