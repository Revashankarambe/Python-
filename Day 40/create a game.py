questions = [
    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,

    "which language was used to create fb?","python","french","java","php","none",4,
     
]

levels = [1000,2000,5000,6000,7000,8000,9000,10000,15000,14000,32000,560000]
money = 0
for i in range(0,len(questions)):
    question = questions [i]
    print(f"question for rs. {levels[i]}")
    print(f"a. {question[1]}    b. {question[2]}")
    print(f"c.{question[3]}     d. {question[4]}")
    reply = int(input("Enter your answer (1-4)"))
    if(reply == questions[-1]):
        print(f"correct answer , you won rs {levels[i]}")
        if(i==4):
            money = 7000
        elif(i==9):
            money = 10000     
    
    else:
        print("worng answer")
        break    









    