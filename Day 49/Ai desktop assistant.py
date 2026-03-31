# x = int(input("enter the value of x:"))

# match x:
#     case 0:
#         print("x is zero")

#     case 4:
#         print("x is 4")

#     case _ if x!=90:
#         print(x,"is not 90")

#     case _ if x!=80:
#         print(x,"is not 80")

# name ='rahul'
# for i in name:
#     print(i)
#     if(i=="h"):
#         print("this is good") 

# colors = ["Red","blue","yellow","chut","gandu"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)   
# 
# for rahul in range(1,50):
#    print(rahul+1 )

# i = int(input("enter the number:"))
# while(1<38):
#     i= int(input("enter the value:"))
#     print(i)
# print("ho gaya bas ab")
# for i in range(12):
#     print("5 X",i+1,"=",5 *( i+1))
#     if(i==9):
#         break
# print("loop chhod kar nikal gaya")  
# i=0
# while True:
#     print(i)
#     i = i +1
#     if(i%100==0):
#         break    
# def calculategmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# a = 9
# b = 8
# # gmean = (a+b)/(a*b)
# # print(gmean) 
# calculategmean(a,b)

# a = int(input("Enter your age:"))
# print("your age is:",a)

# if(a>18):
#     print("you can drive")

# else:
#     print("you cannot drive")    

# a = int(input("enter the age:"))
# print("your age is:",a)
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# if(a>18):
#     print("you can drive")
# else:
#     print("you cannot drive")  

# appleprice = 10
# budget = 200
# int(input("Enter a value:"))
# if(budget - appleprice > 50):
#     print("you can buy")
# elif(budget - appleprice >70):
#     print("ho gaaya lele")
# else:
#     print("tu yeah le nahi skta")                                                                         

# num = int(input("enter a number:"))
# if(num < 0):
#     print("number is negative")
# else:
#     ("number is positive")     
# x = int(input("enter the value of x:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
# name = 'rahul' 
# for i in name:
#     print(i,end=" ")
# for k in range(5):
#     print(k+1) C
# i=0
# while(i<=3):
#     print(i)
#     i=i+1
# print("done with the loop")                
# count = 5
# while(count>0):
#    print(count)
#    count=count-1
# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1
# else:
#     print("i am inside else")
# for i in range(3):
#     print(i)
# i=0
# while(i<=3):
#     print(i)
#     i=i+1
# for i in range(12):
#     if(i==10):
#         break
#     print("5 X",i+1,"=",5*(i+1))
# for i in range(12):
#     if(i==10):
#         print("loop ko chhod kar nikal ")    
  
#         continue
#     print("5 X",i+1,"=",5*(i+1))
# print("loop ko chhod kar nikal ")
# i = 0
# while True:
#     print(i)
#     i = i + 1
#     if(i%100 == 0 ):
#         break
# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# def isGrater(a,b):
#     if(a>b):
#         print("first number is grater")
#     else:
#         print("second number is equal")
# def islesser(a,b):
#     pass               
# a = 9
# b = 8
# isGrater(a,b)
# calculateGmean(a,b)
# # gmean = (a*b)/(a+b)
# # print(gmean)
# c = 8
# d = 7
# isGrater(c,d)
# calculateGmean(c,d)
# gmean = (a*b)/(a+b)
# print(gmean)
# def average(a,b):
#     print("the average is",(a+b)/2)
# average(4,6)
# def name(fname,mname ="rahul",lname="ambe"):
#     print("hello",fname,mname,lname)
# name("Any")    
# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#         print("average is:",sum /len(numbers))

# average(5,6)
# marks = [3,5,6,"rahul",True]
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[5-3])
# print(marks[2])
# def average(a=9,b=1):
#     print("the average is ",(a+b)/2)

# average(5)            
# def name(fname,mname ="rahul",lname ="ambe"):
#     print("hello",fname,mname,lname)
# name("any" )      
# def average(a=9,b=1):
#     print("the average is",(a+b)/2)
# average(b=9)                    
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is:",sum/len(numbers))


# average(5,6)    
# l = [3,4,5,"rahul",True]      
# print(l)
# print(type(l))
# print(l[0])
# print(l[1])  
# marks = [3,5,6,"rahul",True,6,8,9,345,678]
# print(marks)
# print(marks[1:8])
# print(marks[1:8:2])
# tup = (1,5)
# print(type(tup),tup)
# tup = (1,2,76,342,32,"rahul",True)
# if 3421 in tup:
#     print("yes 342 is present in this tuple")
# tup2 = tup[1:4]
# print(tup2)
# countries = ("pakistan","afghanistan","bangladesh","srilanka")
# countries2 = ("vietnam","india","china")
# southEastAsia = countries+countries2
# print(southEastAsia)
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# letter =  "hey my name is {} and i am from {}"
# country = "india"
# name = "rahul"
# print(f"hey my name is   {name} and i am from {country}")
# price = 49.0999
# txt = f" for only {price:2f} dollars!"
# print(txt)
# print(f"{2*3}")
# def square(n):
#     '''Take in number n, returns the square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)    
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# s = {2,4,2,6}
# print(s)
# info ={"carla",19,False,5.9,19}
# s1 = {1,2,5,6}
# s2 = {3,6,7}
# print(s1.union(s2)) 
# s1.update(s2) 
# print(s1,s2)
# marks = int(input("Enter a marks:"))
# if marks>=90:
#     print("this A greate")
# elif marks>=75:
#     print("this B great")
# elif marks>=50:
#     print("this c gerat") 
# else:
#     print("fail")

# age = int(input("Enter the age:"))
# if age>=18:
#     print("vote de sakta hai")
# else:
#     print("this is below 18")
# num1 = int(input("Enter first largest number: "))
# num2 = int(input("Enter second largest number: "))
# num3 = int(input("Enter third largest number: "))
# if num1 >=num2 and num1 >= num3:
#     print(f"largest number is{num1}")
# elif num2 >=num1 and num2 >= num3:
#     print(f"the largest number{num2}")
# else:
#     print(f"the largest number{num3}") 
# num = int(input("Enter the number:"))
# if num>=1:
#     print("number is positive")
# else:
#     print("number is negative")    
# num = int(input("Enter the number:"))
# if num %2 == 0:
#     print(f" {num} is even number")
# else:
#     print(f"{num} number is odd")

# for i in range(1,21):
#     if i %2 ==0:
#         print(i)

# for i in range(0,50):
#     print(i+1)
# for i in range (1,100):
#  if i %3 == 0 and i %5 ==0:
#     print(i)

# num = int(input("enter number:"))
# total = 1
# for i in range(1,num + 1):
#     total = total+1
# print("sum number",total) 
   
# num = int(input("Enter number: "))
# fact = 1

# for i in range(1,num + 1):
#     fact = fact * i
# print("Factorial is:",fact) 

# ep1 = {122:45,123:89,567:69,670:69}
# ep2 = {222:67,566:90}
# ep1.update(ep2)
# # ep1.pop (122)

# print(ep1)

# for i in range(6):
#     print(i)
#     if i ==4:
#         break
# else:
#     print("sorry no i")

# for x in range(5):
#     print("iteration no {} in for loop".format(x+1))
# else:
#     print("else block in loop")
# print("out of loop")                

# for i in range(0,30):
#     if i % 3 == 0:
#         print(i
# total = 5
# for i in range (1,6):
#     total = total * i
# print(total)   

# for i in range (1,20):
#     if i %2  != 0:
#         print(i) 

# for i in range(10,0,-1):
#     print(i)
# try:
#  a = int(input("enter the value:"))
#  print(f"multiplication tablr of{a} is:")


#  for i in range(1,11):
#     print(f"{a} X {i} = {a*i}")
# except Exception as e:
#   print(e)
# print("bas ho gaya code chal reha hai")

# a = int(input("Enter any value b/w 5 and 9:"))
# if(a<5 or a>9):
#     raise ValueError("value should be b/w 5 and 9")
# else:
#     print("code run ho gaya")

       
# char = ['x','y','z'] # ye list mai random letters add hote hai
# encoded = []
# encoded.append("hx")# ye value add karta hai
# msg = "hi"
# encoded[]
# for ch in msg:
#     encoded.append(ch+"x")
# msg = "hxix"

# for i in range(0, len(msg), 2):
#     print(msg[i]) 
# a = 330
# b = 3303
# print("A") if a > b else print("=") if a == b else print("B")

# c = 9 if a>b else 0
# print(c)

# for i in range(1,50):
#     if i %7 == 0:
#         print(i)

# for i in range(1,21):
#     print(f"{i} = {i**3}")
# for i in range(0,30):
#     print(f"{i} = {i*i}")

# num = input("Enter the number:")

# count = len(num)
# for i in range(count):
#     print("loop chal reha hai")
          
# for i in range(1,100):
#    if  i %2!=0:
#     print(i)

# nums = [10,15,20,25,30]

# total = 0

# for i in nums:
#     if i %2==0:
#         total = total+i
# print("even number ka sum",total)        

# num = int (input("Enter number:"))

# total = 0
# for i in range(1,num):
#     if num % i == 0:
#         total = total +i
# if total == num:
#     print("Number is Perfact")
# else:
#     print("Not a Perfact Number")            
 

# for num in range (1,51):
#     if num >1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#             else:
#                 print(num)

# text = input("enter the value:")
# reversed = ""
# for i in range(len(text)-1,-1,-1):
#     reversed = reversed + text[i]
# print("reversed string",reversed)    

# text = "rahul"
# for ra in text:
#     print(ra)

# text = input("Enter the string:")
# reversed = ""

# for ra in text:
#     reversed = ra+reversed
# print(reversed)    

# text = "python"
# rev = ""
# for py in text:
#     rev=py+rev
#     print(rev)

# text = "hello"
# rev="" 
# for ra in text:
#     rev=rev+ra
#     print(rev)

# text = "hello"
# rev = ""
# for ra in text:
#     print(ra)

# text = "rahul"
# rev = 0
# for ra in text:
#     rev=rev+1
# print(rev)

# text = "hello"
# rev = ""
# for ra in text:
#     rev = ra + rev
# print(rev)    

# num = [10,50,30,40]
# num.sort()
# print("second largest",num[-2])

# num = [10,50,30,40]
# num.sort()
# print("largest number",num[-2])

# nums = [1,2,2,3,3,3]

# duplicates = set()
# for i in nums:
#     if nums.count(i)>1:
#         duplicates.add(i)
# print("duplicates value",duplicates)
# print("count",len(duplicates))

# text = "hello"
# rev= ""
# for ra in text:
#     rev=ra+text
#     print(rev)
 
# num = [10,30,60,80]
# num.sort()
# print("second largest number",num[1])

# num = [1,2,2,2,3,3,]

# duplicate = set()
# for i in num:
#     if num.count(i)>1:
#         duplicate.add(i)
# print("duplicate value",duplicate)
# print("count",len(duplicate))        

# import math

# result =math.sqrt(9)
# print(result)

# import math
# num = math.floor(4.23333)
# print(num)

# from math import sqrt,pi

# from math import * 
# result = sqrt(9) * pi
# print(result)

# import math
# print(dir(math))

# def welcome():
#     print("Hey you are welcome")
# if __name__ =="__main__":
#     welcome()
# 
# def welcome():
#     print("hey you are welcome from harry")
# print(__name__)    
# if __name__ == " __main__ ":    
#    welcome()  

# import os
# os. mkdir("data")

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/day{i+1}")
# st = input("Enter message :")
# coding = True
# if(coding):
#     nwords = []
#     words = st.split()
#     for word in words:
#         if(len(word)>=3):
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew = r1 + word[1:] + word[0]+r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word)    
#     print("".join(nwords))    
# else:
#     pass 
     
# x = 4
# print(x)

# def hello():
#     print("hello rahul")

# for i in range(0,20):
#     if i %2 == 0:
#         print(i)

# for i in range(1,20):
#     if i %2!= 0:
#         print(i)

# for i in range(1,11):
#     print(f"{i}{i*i}")

# total = 0
# for i in range(1,11):
#     total= total+i
# print("sum is:",total)    

# total = 5
# for i in range(1,50):
#     total=total/i
# print("divide",total) 

# num = int(input("Enter the value:"))
# for i in range(0,11):
#     num=num*i
# print("mutplication",num)       

# num = int(input("Enter the number:"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# total = 0
# for i in range(1,50):
#     total=total+i
# print("sum number",total)    

# text = "hello"
# # for text in text():
# for i in text:
#     print(i)

# for i in range(0,20):
#     if i % 2!=0:
#         print(i)

# num = int(input("Enter a number:"))

# sum_digits = 0

# while num > 0:
#     digits = num % 10
#     sum_digits += digits
#     num = num // 10
# print("sum of digits:",sum_digits) 

# num =123
# sum = 0

# while num>0:
#     digit = num % 10
#     sum += digit
#     num = num //10
# print(sum)   

# num = 456
# sum = 0 
# while num>0:
#     digit = num%10
#     sum+=digit
#     num = num//10
# print(sum)    

# num = int(input("Enter the value:"))
# sum = 0
# while num >0:
#     digit = num%10
#     sum+=digit
#     num = num//10
# print(sum) 

# for i in range(1,20):
#     if i % 2!=0:
#         print(i)

# num = int(input("Enter the value:"))
# if num>=0:
#     print("Number is positive")
# else:
#     print("number is negitive")   

# num = 5
# print(f"{num} is odd and  positive number")

# num = int(input("Eneter the table:"))

# for i in range(1,11):
#     print(f"{num} X {i} = {num * i}")

# num = int(input("Enter the value:"))
# sum = 0 
# while num>0:
#     digit = num%10
#     sum+=digit
#     num = num//10
# print(sum)    

# num = int(input("Enter the value:"))
# if num<6:
#     print("weak password")
# elif num <= 10:
#     print("password is medium")  
# else:
#     print("pass is strong")

# num = int(input("Enter the value:"))
# rev=0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print(f"{rev}")    

#  num = int(input("Enter the number:"))
# rev = 0
# while num > 0:
#     digit = num% 10
#     rev = rev * 10 + digit
#     num = num // 10
# print(f"{rev}")   

# num = int(input("Enter a number:"))
# if num <= 1:
#     print(f"{num} is not  a prime number")
# else:
#     is_prime = True
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime numbers")       


# secret = 7

# guess = int(input("guess the number:"))

# while guess != secret:
#     if guess > secret:
#         print(f"{guess} is to high!")
#     else:
#         print(F"{guess} is too low!")
#     guess = int(input("Try again:")) 
# print(f"correct! the number was {secret}")    

# even_sum = 0
# odd_sum = 0
# for i in range(1,11):
#     if i %2 == 0:
#         even_sum +=i
#     else:
#         odd_sum +=i
# print(f"sum of even number {even_sum}")
# print(f"sum of odd number {odd_sum}")            

# correct_password = "1234"
# correct_username = input("Enter a name:")
# attempts = 3

# while attempts > 0 :
#     username = input("Enter username: ")
#     password = input("enter password:")

#     if username == correct_username and password == correct_password:
#         print(f"Login successful")
#         break
#     else:
#         attempts -= 1
#         print(f"worng password attempts left {attempts}")
# if attempts == 0:
#     print("account locked")  

# num = int(input("Enter the value:"))

# if num == 0:
#     print("Number is zero")


# elif num % 2 == 0:
#     print(f"{num} number is even")

# # elif num<=0:
# #     print("Zero")

# else:
#     print(f"{num} number is odd")   

# num = int(input("Enter The value:"))
# if num>0:
#     print(f"{num} Number is positive")
# elif num<0:
#     print(f"{num} Number is negative")
# else:
#     print("Number is  Zero")
# 
#            
# number = int(input("Enter the value :"))
# if number % 3 == 0 and number % 5 == 0:
#     print("fizz buzz")
# elif number % 3 == 0:
#     print("fizz") 
# elif number % 5 == 0:
#     print("buzz") 
# else:
#     print("normal number") 
#    
fizz = 0
buzz = 0
fizzbuzz = 0
normal = 0
for i in range(1,51):
    if i %3 == 0 and i % 5 == 0:
        print(f"{i} fizzbuzz")
        fizzbuzz += 1
    elif i%3 == 0:
        print(f"{i} fizz") 
        fizz += 1  
    elif i%5 == 0:
        print(f"{i} buzz")
        buzz += 1   
    else:
        normal+=1       
print(f"\nfizz count: {fizz}")
print(f"buzz count: {buzz}")
print(f"buzz count: {fizzbuzz}")
print(f"cont normal { normal}")      
