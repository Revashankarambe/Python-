import random

secret = random.randint(1,100)

level = input("choose difficulty:").lower()

if level == "easy":
    secret = random.randint(1,50)

elif level == "medium":
    secret = random.randint(1,100)    

elif level == "hard":
    secret = random.randint(1,500)
else:
    print("invalid choice,default medium")
    secret = random.randint(1,100)
# secret = random.randint(1,100)

atteamp = 5
count = 2
print(f" you have {atteamp- count} attempts left")
# atteamp_Left = 5
while count < atteamp:
    guess = int(input("Enter the guess :"))
    count += 1

    if guess > secret:
        print("too high")
        # count += 1
        # atteamp_Left = 5

    elif guess < secret:
        print("too low")

    # elif atteamp > 5:
    #     print("game over")     

    else:
        print(f"correct you gussed in {count} attempts")
        break
    print(f"Attempts left:{atteamp - count}")
    print(f"you have only {atteamp -  count} attempts left!")
if count == atteamp and guess != secret:
    print("game over")
    print(f"the correct number was {secret}")

# print= {count}        
               