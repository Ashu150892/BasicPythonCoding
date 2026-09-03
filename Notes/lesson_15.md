# Lambda Functions
A lambda is a small function that you can write in one line.

1. Normal Function:
def square(num):
    return num * num

2. Lambda Function:
square = lambda num: num * num

# Meaning of lambda num: num * num
Take num and return num * num

## lambda parameter: expression

square = lambda x: x * x
multiply = lambda a, b: a * b

**   Use a lambda when the function is very small and simple.

# Normal loop:
doubled = []

for num in numbers:
    doubled.append(num * 2)

##  With map() and lambda:

doubled = list(map(lambda num: num * 2, numbers))
map() applies the lambda to every element:

# map() =   list(map(function, collection))
# map() + lambda = list(map(lambda x: expression, collection))

map() changes/transforms every item.
filter() selects items based on a condition.

list(filter(lambda x: x % 2 == 0, numbers))
here x%2== 0 if true then filter() work otherwise not work

# reduce() = Take a collection of values and repeatedly combine them until only one result remains.

reduce(lambda a, b: a + b, numbers)
Take two values, add them, use the result with the next value, and continue.

# Functional Tools:
map()     → transform
filter()  → select
reduce()  → combine
