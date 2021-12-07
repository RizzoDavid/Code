import random 
passlen = int(input("How long would you like the password to be?"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[{]}\|;:'<,>.?/"
p = "".join(random.sample(s,passlen ))
print(p)
