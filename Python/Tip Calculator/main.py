#This will calculate how much a person should pay after tip. 

#Welcome Infromation
welcome_message = "Welcome to the tip generator. This tool will help you determine how much of a tip to leave."
print(welcome_message)

# Input information
bill = float(input("What is the total cost of the bill? ").strip('$')) #.strip('$') will remove the $ from the input. 
people = float(input("How many people are splitting the bill? "))
tip_percent = float(input("What percentage would you like to tip? i.e. 10, 15, 20 ").strip('%')) #.strip('%') will remove the % from the input.

#Math
tip = (tip_percent / 100) + 1
total = "%0.2f" % ((bill / people) * tip) #"0.2f" % x ensures that ther are always 2 decimal places. 
tip_amount = "%0.2f" % (float(total) - (bill / people)) 

# Print
print(f"Each person should pay ${total}. The tip is ${tip_amount} per person.")

