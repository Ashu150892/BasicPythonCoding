marks = float(input("Enter your marks"))
if marks>=90:
  print("A")
elif marks>=75:
  print("B")
elif marks>=60:
  print("C")
elif marks>=35:
  print("D")
else:
  print("Fail")

month_number = int(input("Enter the month number :"))
if month_number ==12 or month_number ==1 or month_number ==2:
   print("Winter")
elif month_number ==3 or month_number ==4 or month_number ==5:
   print("Summmer")
elif month_number ==6 or month_number ==7 or month_number ==8 or month_number ==9:
   print("Monsoon")
elif month_number ==10 or month_number ==11:
   print("Autumn")
else:
    print("Invalid Month")

salary = float(input("Enter the Salary"))
if salary < 25000:
   print("Low Income")
elif salary == 25000 or salary <=50000:
   print("Medium Income")
else:
   print("High Income")