#Take a two digit number and add the first digit to the second digit

two_digit_number = input("Type a two digit number: ")

#seperate two digit number into 2 1 digit numbers
first_num = two_digit_number[0]
second_num = two_digit_number[1]

#convert the string into integer 
first_num_int = int(first_num)
second_num_int = int(second_num)

#Math Equation
solution = first_num_int + second_num_int

#Convert Solution to string
solution_stg = str(solution)

#Print the addtion of the two numbers
print(first_num + " + " + second_num + " = " + solution_stg)
print(solution)