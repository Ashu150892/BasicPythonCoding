print("Enter your Card")
input("Click Enter")
pin_num = int(input("Enter your valid pin"))
amount =3000
if(pin_num==4567):
    print("Valid Pin")
    enter_amount= float(input("Enter amount: "))
    if(enter_amount>amount):
       print("No amount is avaiable")
    else:
        print("Please collect the cash")   
else:
    print("Invalid Pin")

act_amount=10000
act_pin = 5555
enter_amount_value= int(input("Enter the amount :"))
if enter_amount_value>=act_amount:
    print("Insufficient Balance")
elif enter_amount_value<=act_amount:
    enter_pin =int(input("Enter the pin"))
    if act_pin == enter_pin: 
            print("Pin Validated")
            print("Collect your cash")
    rem_amount=act_amount-enter_amount_value
    print("The remaining amount is :", rem_amount)
    act_amount = rem_amount
    agn_amount = int(input("Enter the amount again :"))
    if agn_amount<act_amount:
         print("Please collect again cash")
    if act_amount ==0: 
         print("Insufficent balance")
    else:
       print("Sorry")
else:
    print("Incorrect Pin")








