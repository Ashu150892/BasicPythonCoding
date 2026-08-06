weight = float(input("Enter your weight in kg :"))
height = float(input("Enter your height in m :"))

calc_bmi= weight/(height*height)
if calc_bmi <18.5:
    print("Value of BMI :", calc_bmi)
    print("Category : Underweight")
elif calc_bmi >=18.5 and calc_bmi <=24.9:
    print("Value of BMI :", calc_bmi)
    print("Category : Normal")
elif calc_bmi >=25 and calc_bmi <= 29.9:
    print("Value of BMI :", calc_bmi)
    print("Category : Overweight")
else:
    print("Value of BMI :", calc_bmi)
    print("Category : Obese")