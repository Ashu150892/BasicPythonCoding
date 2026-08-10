## A loop repeats the same block of code multiple times.
## Python has two main loops:
      for loop ✅
      while loop ✅

## A for loop is used when you know how many times you want to repeat something.

## Syntax:
     for variable in range(start, stop, increment/decrement):
     print(variable)

## print()
        # By default it goes to next line automatically --> Vertical
        # to print in hozitontal use end parameter inside print

# print(i)  ---> Vertical
# print(i, end=" ") --> Horizontal


## end → What to print after the value (default is a new line \n).
#   sep → What to print between multiple values.


## A while loop is used when you don't know how many times something should repeat.

# Syntax:
   while condition:
    # Code to repeat

# Initialze --> Check the Condition till is it true --> print --> increase the initializer.

# If you will not stop. This is called an Infinite Loop

## break
   Stops the loop completely
   Execution comes out of the loop

## continue
   Skips only the current iteration
   Execution goes to the next iteration

### Explanation of Looping
   
   for i in range(3)
     for j in range(i)
     print(j)

## for i in range(A):
    for j in range(B):

# Rows    = A
  Columns = B
  Total iterations = A × B