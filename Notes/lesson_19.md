# Modules and packages help us organize our code.

A module is simply a Python .py file containing code that we can reuse.

# Syntax:

class_name.py

def function_name_01():
    return

def function_name_01():
    return

Now Import

import class_name

result = class_name.function_name()
print(result)

1. Import Specific Functions

from class_name import function_name_01
print(function_name_01())

2. Import multiple functions

from class_name import function_name_01, function_name_02
print(function_name_01())
print(function_name_02())


## Using as — Give a Module an Alias
Sometimes module names are long

import class_name as short_name



### Python Packages:

A package = a folder containing multiple Python modules.

Syntax:

from package_name.class_name import function_name


1.  __init__.py:
__init__.py is a special Python file associated with a package.

it help in initialization/setup file for a package


.py file       → Module
Folder         → Package
__init__.py    → Package initialization/organization file


Folder/package --> File name(.py) --> function_name()



### External Packages and pip:

| Package      | Common use             |
| ------------ | ---------------------- |
| `requests`   | API/HTTP requests      |
| `pandas`     | Data analysis          |
| `numpy`      | Numerical calculations |
| `matplotlib` | Charts/graphs          |
| `openpyxl`   | Excel files            |
| `selenium`   | Browser automation     |


1. What is pip?

pip is Python's package installer.

Download command:  pip install requests



