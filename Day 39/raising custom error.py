a = int(input("enter a value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")