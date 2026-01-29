def fun1():
    try:
        l=[1,5,6,7]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("i am always executed")

x = fun1()
print(x)         