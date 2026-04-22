num = int(input("Enter the value :"))
total = 0
while  num >0:
    digit = num % 10
    total += digit
    num = num // 10
print(total)