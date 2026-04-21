import random
import string
password = ""

letters = string.ascii_letters + string.digits + string.punctuation

choose = input("choose(1/2/3) :")
length = int(input("Enter password lrngth:"))

if choose == "1":
   chars = string.ascii_letters

elif choose == "2":
   chars = string.ascii_letters + string.digits

elif choose == "3":
   chars = string.ascii_letters+string.digits+string.punctuation

else:
   print("invalid choice")
   chars = string.ascii_letters         

if length <=0:
    print(f"{length} invalid length")

else:
 for i in range(length):

    password += random.choice(chars)

print(f"your password is: {password}")    