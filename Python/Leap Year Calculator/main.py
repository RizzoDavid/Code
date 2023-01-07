year = (int(input("Which year do you want to check?")))

#Math
year4 = year % 4
year100 = year % 100
year400 = year % 400

#If Then Print
if year4 == 0:
    if year100 == 0:
        if year400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")