## File Handling means allows Python programs to create, read, write, and modify files.

1. Create --
2. Read --
3. Write --

# open():
Syntax:
open("filename", "mode")

| Mode  | Meaning         |
| ----- | --------------- |
| `"r"` | Read            |
| `"w"` | Write           |
| `"a"` | Append          |
| `"x"` | Create new file |

# Python automatically closes the file after the with block.

with open("file_name",'mode') as file
     content=file.mode
     print(content)


# 🔥 Main Difference
# Method	      What it returns	                 Example
read()	        Entire file as string	  "Python\nAI\nMachine Learning"
readline()    	One line as string	              "Python\n"
readlines()	    All lines as a list	       ["Python\n", "AI\n", ...]

# Write() : returns the number of characters written
## the old content is deleted/overwritten.

# CSV

csv.reader()     → Read CSV
row[index]       → Access columns
csv.writer()     → Create a writer
writer.writerow() → Write one row


## JSON:

1. JSON stands for:  JavaScript Object Notation

json.load()
     ↓
JSON file → Python object

json.dump()
     ↓
Python object → JSON file


##
csv.reader()   → Read CSV
csv.writer()   → Write CSV

json.load()    → Read JSON
json.dump()    → Write JSON



#
Dictionary → use key    {}
List       → use index  []

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)