# Exception Handling: 
An exception is an error that happens while your program is running.
Exception handling allows us to handle the error instead of allowing the program to crash.

# Syntax:
 
try:
    # code that may cause an error
except:
    # code to handle the error

1. else
else runs only when there is no exception.

# Syntax: 
 try:
 # code
 except:
 # code
else: 
 # code

## 
try
 ↓
Error?
 ├── YES → except
 │
 └── NO  → else

# finally
finally runs whether an error occurs or not.

##

try:
    # risky code

except SomeError:
    # handle error

else:
    # runs if no error

finally:
    # always runs

###

TRY
 ↓
Try something
 ↓
Did error happen?
 ↓
YES → EXCEPT
NO  → ELSE
 ↓
FINALLY
 ↓
Always executes


## raise
When we want to tell Python that something is wrong ourselves.

raise
  ↓
CREATE / THROW an exception

except
  ↓
CATCH / HANDLE an exception