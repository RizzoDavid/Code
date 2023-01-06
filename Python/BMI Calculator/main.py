height = input("enter your height in inches: ")
weight = input("enter your weight in lbs: ")

#Convert inputs to float
height_fl = float(height)
weight_fl = float(weight)

#Convert imperial to metric
heightm = height_fl * 0.0254
weightm = weight_fl * 0.45359237

# BMI Calculation

bmi = weightm / heightm ** 2
bmi_round = round(bmi)

#Print BMI

if bmi <= 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi_round}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi_round}, you are obese.")
else:
    print(f"Your BMI is {bmi_round}, you are clinically obese.")