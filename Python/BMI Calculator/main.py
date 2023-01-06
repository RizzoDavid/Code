height = input("enter your height in inches: ")
weight = input("enter your weight in lbs: ")

#Convert inputs to float
height_fl = float(height)
weight_fl = float(weight)

#Convert imperial to metric
heightm = height_fl * 0.0254
weightm = weight_fl * 0.45359237

# BMI Calculation

bmi = round(weightm / heightm ** 2)

#Print BMI

print(int(bmi))