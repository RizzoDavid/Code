#Calculator that determines approximatley how many more months, weeks, and days you have left with a 90 year life expectancy based on your current age. 

age = input("What is your current age? ")

#Covnert Age to integer
age_int = int(age)

#How Many weeks and days in 90 years
lifeweek = 90 * 52
lifeday = 90 * 365
lifemonth = 90 * 12

#Calculate Current amount of days/weeks lived
currentweek = age_int * 52 
curretnday = age_int * 365
currentmonth = age_int * 12

#Calculate How many days, weeks, and years left
remaining_months = lifemonth - currentmonth
remaining_weeks = lifeweek - currentweek
remaining_days = lifeday - curretnday

#Print Results
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")