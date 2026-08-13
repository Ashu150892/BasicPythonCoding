list_data= []                     # Empty

age =[24, 56, 58, 72, 60]
print("Length of age array :", len(age))
age.append(67)
print("Length of age array after append :", len(age))


marks_score =[]
for marks in range(5):
    marks = int(input("Enter the Marks :"))
    marks_score.append(marks)
print(marks_score)


marks =[]         # Empty list
for i in range(5):
    mark=int(input("Enter the marks :"))
    marks.append(mark)
print(marks)
total=sum(marks)
print("Total :", total)
avg=total/len(marks)
print("Aveage :", avg)
highest=max(marks)
print("Highest :",highest)
lowest=min(marks)
print("Slowest :",lowest)
#even_marks =["Even" if i % 2==0 else "not even" for i in marks ]
even_marks = [i for i in marks if i % 2 == 0]
print(even_marks)
marks.sort()
print("Sorted marks:", marks)
for marks_report in marks:
   if marks_report>=40:
      print(marks_report, "Pass")
   else:
       print(marks_report, "Fail")