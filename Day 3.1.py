Height=float(input("please enter your height in m :"))
Weight=float(input("Please enter your weight in kg : "))
BMI=round(Weight/Height**2)
if(BMI<18.5):
    print(f"your BMI is {BMI},you are underweight")
elif( BMI<25 ):
        print(f"your BMI is {BMI}, you are normal weight ")
elif(BMI<30):
        print(f"your BMI is {BMI}, your are over weight")
elif(BMI<35):
        print(f"your BMI is {BMI}, your are obese ")
else:
    print(f"your BMI is {BMI}, you are clinically obese")