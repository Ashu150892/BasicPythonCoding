# Recursion :  When Function call itself. It depends on base case. Without base case it will keep calling. 

def function_name(n):
    Condition:
    print()
    function_name(n - 1)

function_name(value)

# Recursive case — function calls itself:

Recursive function
       ↓
  Base case?
   ↙       ↘
Yes         No
 ↓           ↓
Stop       Call itself