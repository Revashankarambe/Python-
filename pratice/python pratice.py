# from math import sqrt,pi
# from math import*
# result = sqrt(9) * pi 
# print(result)

# import os
# if(not os.path.exists("data")):
#  os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/day{i+1}")

# f = open('practice question')
# i=0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     print(line)
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student 1 in maths is: {m1}")    
#     print(f"marks of student 1 in maths is: {m1}")    
#     print(f"marks of student 1 in maths is: {m1}")    
     

    # if not line:
    #     break
    # print(line)

# num = int(input("Enter the value:"))

# for i in range(2,num):
#     if num % i == 0:
#         print("not prime")
#         break
#     else:
#         print("Prime")

# num = int(input("Enter the value:"))
# if num % 2 == 0:
#   print(f"{num} is even")
# else:
#  print(f"{num} is odd") 
# 
# num = int(input("Enter the value:"))
# total = 0 

# while num > 0:
#     digit = num % 10
#     total = total + digit
#     num = num // 10 
# print("sum of digits:",total)   
# 

# num = input("Enter number: ")
# total = 0

# for i in num:
#     total += int(i)
# print(total)    

# num = input("Enter the value :")
# total = 0

# for i in num:
#     total +=(i)
# print(total)
# 
# num = int(input("Enter the value"))
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev*10+digit
#     num = num//10
# print("reverse",rev)    

# num = int(input("Enter the number :"))
# if num > 0:
#     print(" number is Positive")
# elif num == 0:
#     print("number is zero")  
# else:
#     print("number is Nagative")   
# 
# num1 = int(input("Enter the number :"))
# num2 = int(input("Enter the number :"))

# if num1 > num2 :
#     print("largest number ",num1)
# else:
#     print("lowest number",num2)    

# num1 = 10
# num2 = 50
# num3 = 30

# if num1 >= num2 and num1 >= num3:
#     print("largest number",num1)
# elif num2 >= num1 and num2 >= num3:
#     print("largest number",num2)
# else:
#     print("this is lowest number",num3)        

# num1=10
# num2=50
# num3=30
# if num1 <=num2 and num1 <= num3:
#     print("lowest number",num1)
# elif num2<= num1 and num2<=num3:
#     print("lowest number",num2)
# else:
#     print("lowest number",num3)

# n = int(input("Enter number:"))
# total = 0
# for i in range(1,n+1):
#     total = total + i
# print("sum is:",total) 
# 
# n = 5
# total = 0

# for i in range(1,n+1):
#     total+=i
# print(total)
# 
# factorial       

# n = 5
# fact = 1

# for i in range(1,n+1):
#     fact *=i
# print("factorial",fact)    

# num = int(input("Enter the value :"))
# for i in range(0,51):
#     if i % 2 == 0:
#      print("even number")
#     else:
#        print("odd")
# 
#even number ka total
# total = 0

# for i in range(1,51):
#     if i % 2 == 0:
#         total += i
# print("sum of even number:",total)

#odd numbers ka total
# total = 0

# for i in range(1,51):
#     if i % 2!=0:
#         total +=i
# print("sum of odd number",total) 
# 
# 1 se 100 tak number print karo
# jo 3 aur 5 dono se divide hote ho

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i) 
# 
#  Count karo  
# 1 se 100 tak kitne numbers  
# 3 se divide hote hain    

# count = 0
# for i in range(1,101):
#     if i % 3 == 0:
#         count +=1
# print("count of this number",count)    
# 
# 1 se 100 tak numbers me 
# kitne even hain sur kitne odd hain
# 
# even_count = 0
# odd_count = 0
# for i in range(1,101):
#     if i % 2==0 and i % 2!=0:
#         even_count +=1
#     else:
#         odd_count +=1
# print("this is a number",even_count)
# print("this is a number",odd_count)                            

# 1 se 100 tak numbers me
# largest even number kaun sa hai?      
# max_even = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         if i > max_even:
#             max_even = i
# print("largest even number",max_even)        

# 1 se n tak numbers print karo jo 5 se divide hote ho
# n = int(input("Enter number:"))
# for i in range(1,n+1):
#     if i % 5 == 0:
#         print(i)

#1 se n tak numbers ka sum nikaalo
#sirf even numbers ka
# n = int(input("Enter the number:"))
# total = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         total +=i
#         print( "this is a even number",total)

#user se number lo
#check karo wo palindrone hai ya nahi
#(121>yes,123>no)
# num = int(input("Enter number:"))
# original = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if original == rev:
#     print("palindrome")
# else:
#     print("Not palindrome")   
# 
num = input("Enter number:")
if num ==num[::-1]:
    print("palindrome")
else:
    print("not palindrome")

         

 
 
 