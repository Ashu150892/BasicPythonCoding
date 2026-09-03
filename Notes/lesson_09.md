## A function is a reusable block of code that performs a particular task.

## Steps:
   Create a function  --> using def keyword
   Call the function 

## Syntax:
    def function_name():     ---> Creating function
       statement

    function_name()          ---> Calling function

# def --> define a function, it is reversed word in python.

## Parameterised & Non Parameterised:
--> def function_name(perameter):
        print("Hello", parameter )

    function_name(argument)
## argument is basically value

## Return
return allows us to take the value produced by a function and use/reuse it outside the function.

# Syntax:
def function_name(parameter):
    return parameter
value_store= function_name(argument)
print(value_store)

Example:  def sum(a, b)
             return a+b
          sum_val=sum(x,y)
          print(sum_val)

# In case of multiple argument we received:
def add_numbers(*args):
    print(args)

# *args = Accept any number of positional arguments. (As tuples)

# **kwargs = (As Dictionary)
1. *args handles multiple positional arguments.
2. **kwargs handles multiple keyword arguments.

def student_details(**kwargs):
    print(kwargs)

example:

def student_details(variable="value", variable="value", variable="value"):
    print(kwargs)

# 
1. def student_details(**kwargs):
      for key, value in kwargs.items():
         print(key, ":", value)