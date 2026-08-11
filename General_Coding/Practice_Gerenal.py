marks = [70, 85, 60]
marks.append(90)
marks.insert(1,75)
marks.remove(60)
last_marks = marks.pop()
print("Final Marks :", marks)
print("Removed Marks :", last_marks)


numbers = [2, 4, 6, 8]
double =[i*2 for i in numbers]
print(double)


numbers = [5, 10, 15, 20, 25, 30]
multiples_of_10 = [num*10 for num in numbers if num %10 ==0]
print(multiples_of_10)

numbers = [10, 15, 20, 25, 30]
result = ["Big" if num >=20  else "Small" for num in numbers]
print(result)

numbers = [1, 2, 3, 4, 5, 6]
new_list=[i*i if i%2==0 else i*i*i for i in numbers]
print(new_list)
