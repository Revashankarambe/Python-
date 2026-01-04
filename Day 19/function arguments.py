# def average(a=9, b=1):
#     print("the average is",(a+b)/2)
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum + i
    return sum / len(numbers)
    
c= average(5,6,7,8)
print(c)
         
# average(5,6)        
# average(b=9)    