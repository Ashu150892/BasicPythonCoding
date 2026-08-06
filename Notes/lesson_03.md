## Data Type -- It basically define the type of data or what kind of data we are storing.
We have 4 types of Data_type:
str --> String - Contain text in single quote, double & triple quote.
int --> Integar - Contain whole number
float --> Decimal value
bool -->Boolean - True or False
## There is one funtion called type() is used to find out the type of data store.
In Python's float is usually based on a 64-bit floating-point number (IEEE 754). Otherwise no limit for the other data type.
To check limit of the float we have the below command:
                   import sys
                   print(sys.float_info)

## Python provides formatting.
         average = 8 / 3
         print(f"{average:.2f}")
    ## We have f-Strings function