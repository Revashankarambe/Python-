balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount >= balance:
    print("Withdraw Successful")
else:
    print("Insufficient Balance")
