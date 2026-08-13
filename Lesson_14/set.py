set_list={}                  # Empty

marks ={30, 45, 55, 65, 75}
print("Original Set of Marks :", marks)
print(type(marks))
marks.add(95)
marks.add(55)
print("Set after adding :",marks)
# marks.remove(85)                  -- Throw Error
marks.remove(55)
print("Mark before discard :",marks)
marks.discard(85)
print("Mark after discard :",marks)

new_marks_set ={90, 70, 75}

add_marks_set =marks.union(new_marks_set)
print("Union :",add_marks_set)

add_marks_set =marks.intersection(new_marks_set)
print("Intersection :",add_marks_set)

add_marks_set =marks.difference(new_marks_set)
print("Difference :",add_marks_set)

add_marks_set =marks.symmetric_difference(new_marks_set)
print("Symmetric Difference :",add_marks_set)