marks_nested=[[78,65,89],[75,70,78],[90,96,98]]
print(marks_nested[0])                          # Accessing single
print(marks_nested[1])
print(marks_nested[2])
print(marks_nested[0][0])                       # Accessing Individual Element of Inner list
print(marks_nested[0][1])
print(marks_nested[0][2])
print(marks_nested[1][0])
print(marks_nested[1][1])
print(marks_nested[1][2])
print(marks_nested[2][0])
print(marks_nested[2][1])
print(marks_nested[2][2])

for row in marks_nested:
    for value in row:
        print(value, end=" ")
    print()

for i in range(len(marks_nested)):
    print("Row", i + 1, "Sum:", sum(marks_nested[i]))
