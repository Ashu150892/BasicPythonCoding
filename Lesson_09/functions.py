def greet():
    print("Hello")
greet()

def print_number(a, b):
    print(a , b)
print_number(10, 20)


num_1= int(input("Enter the 1st number :"))
num_2= int(input("Enter the 2nd number :"))
def add_num(num_1,num_2):
    print("Sum :", num_1+num_2)
add_num(num_1,num_2)


def return_function(a,b):
    return(a*b)
value_return= return_function(5,6)
print(value_return)


a = int(input("Enter the 1st number :"))
b= int(input("Enter the 2nd number :"))
def subtract(a,b):
    return (a-b)
sub_value= subtract(a, b)
print(sub_value)