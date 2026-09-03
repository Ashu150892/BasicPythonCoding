file = open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt",'r')
content = file.read()
print(content)
file.close()

with open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt", "r") as file:
    content = file.read()
    print(content)


file = open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt",'r')
print(file.read())
file.close()

with open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt", "r") as file:
    line = file.readline()
    print(line)

with open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt", "w") as file:
      data_added=file.write("Python is highly demanded language due to AI/ML")
      print(data_added)

with open(r"C:\Users\amadhukar\OneDrive - Lenovo\Desktop\Python.txt", "a") as file:
    data_append=file.write("\nSelenium")
    print(data_append)

lines = [
    "Python\n",
    "AI\n",
    "Machine Learning\n"
]

with open("Python.txt", "w") as file:
    file.writelines(lines)

import os


if os.path.exists("Python.txt"):
    print("File exists")
else:
    print("File does not exist")

    
if os.path.exists("Python1.txt"):
    print("File exists")
else:
    print("File does not exist")