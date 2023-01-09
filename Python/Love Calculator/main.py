#General Information
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Strip Case
name1 = name1.lower()
name2 = name2.lower()

#Set value for variables
true=0
love=0


#Name 1 Counting
true += name1.count('t')
true += name1.count('r')
true += name1.count('u')
true += name1.count('e')
love += name1.count('l')
love += name1.count('o')
love += name1.count('v')
love += name1.count('e')

#Name 2 Counting
true += name2.count('t')
true += name2.count('r')
true += name2.count('u')
true += name2.count('e')
love += name2.count('l')
love += name2.count('o')
love += name2.count('v')
love += name2.count('e')

#Set Love Score Value
lovescore = int(f"{true}{love}")

#If Statements
if (lovescore < 10) or (lovescore > 90):
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif (lovescore > 40) and (lovescore < 50):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")