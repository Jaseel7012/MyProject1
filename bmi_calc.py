
hei=float(input("Enter your height in cm"))
wei=float(input("Enter your weight in kg"))
height=hei/100
BMI=wei/height**2
print("your body mass index is..",BMI)
if BMI>0:
    if BMI<18.5:
        print("you are underweight")
    elif BMI<=25:
        print("you are healthy")
    elif BMI<=30:
        print("you are overweight")
    else:
        print("severely overweight")
else:
    print("enter valid details")