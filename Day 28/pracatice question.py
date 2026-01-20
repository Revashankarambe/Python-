#num = [ 10 ,20,30,40]
#print(num[3])

#name = ["ram","shyam","mohan"]
#for i in range(len(name)):
     #print(name[i])

#num = [1 ,2 , 3 , 4 ,5]
#for i in range(len(num)):
    #print(num[i])
#num = [1,2 ,3 ,4,5,6,7,8,9]
#for n in num:          # loop start
    #if n % 2 == 0:     # even check
        #print(n)       # tabhi print

#num = int(input("Enter the value: "))

#if num % 2 == 0:
 #   print(num, "even number")
#else:
    #print(num, "odd number")
#num = [5,2,9,1]
#big = num[0]
#for n in num:
    #if n>big:
        #big = n
#print("this is big nuber",big) 

num = [-1, -2, 3, -4, 5, -6]
for n in num :
 if n>=0:
    print(n,"number is positive")
else:
    print(n,"number is negative")    

num = []
for i in range (6):
   n= int(input("enter a number: "))
   num.append(n)
print("your list number",num) 


question = [" what is your name"]
option = ["1. rahul,2. shyam,3. rewa,4. ambe"]

answer = [1]
price = [5000]
money = [5000]

for i in range(len(question)):
   print("\n",question[i])
   for opt in option[i]:
      print(opt)
      ans = int(input("enter your anser:"))
      if ans == answer[i]:
         money=price[i]

         print("correct answer",money)
      else:
         print("galat answer")
         break
      

 
print("\n","game over")
print("total money:",money)       

         



   

   



        
