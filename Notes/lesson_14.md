# A set is a collection that stores unique values.
## Syntax:
    set={value_1,value_2, value_3}
## Don't allow Duplicate

## 
List → duplicates allowed
Tuple → duplicates allowed
Set  → duplicates NOT allowed

# Sets don't use indexes

1. A ^ B --> symmetric_difference
2. A | B --> Union

## Method	                   Meaning
union()	                       Everything from both
intersection()	               Common to both
difference()	               In first, not second
symmetric_difference()	       Not common to either

##
1. Subset → smaller/contained set
2. Superset → larger/containing set

### :
add()                    → add one element
remove()                 → remove; error if missing
discard()                → remove; no error if missing

union()                  → everything from both
intersection()           → common elements
difference()             → first set minus second
symmetric_difference()   → elements not common

issubset()               → is A contained in B?
issuperset()             → does A contain B?
isdisjoint()             → no common elements?