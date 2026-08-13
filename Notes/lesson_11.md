## List is like container which contain multiple items.

## It use square bracket to store data.
    variable_name = [value_1, value_2, value_3, value_4, value_5]

## It contain different kinds of data_types.

## It work on the concept of Indexing. Indexing starts with 0.
     variable_name = [value_1, value_2, value_3, value_4, value_5]
     print(variable_name[index_number])
# Python also allows counting from the end. --> Negative Index
   --> from last item.

## Lists are mutable. -- It can be changes.

## append()  --- Add one item to the end of the list.
   variable_number.append(value)

## expend() --  Adds the elements individually

## Method	    Purpose
append()	   Add one item
extend()	   Add multiple items
remove()	   Remove a value
pop()	       Remove by index / last item
len()	       Number of items

## Slicing : access multiple items at once

# Syntax: 
      list[start:end]
      where start -- Includes
            end   -- Excludes

       list[start:end:step]
            step -- Jump means skip
# Reverse a List :
      numbers[::-1]

## sort() modifies the original list. It doesn't create a separate sorted list. Small to large

# numbers.sort(reverse=True)  --> largest to smallest

## reverse() --- Simply reverses the current order:

## Python lists allow duplicate elements, and duplicates are counted when you use len() and count().

## 
if value in list:
   #something

## insert() 
-- list.insert(index, value)
-- insert() doesn't replace the existing item.
-- It pushes the existing item and everything after it to the right

## pop()
 1. Removes the item from the list
 2. Returns the removed item

remove(value) → remove by VALUE
pop(index)    → remove by INDEX

# List comprehension:
   # [new_value for item in list if condition]

[new_value for item in numbers if condition]
   ↑              ↑               ↑
  WHAT?         FROM?           WHICH?

## [value_if_true if condition else value_if_false for item in list]

## Nested List --> List that contain the list inside it.
    -- marks[ row ][ column ]