# factorial (7) = 7*6*5*4*3*2*1 this is a meaing in factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(5 * 4 * factorial(3))    