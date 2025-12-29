import time
hour= int(time.strftime('%H'))
if hour <12:
    print("good morning")
elif hour <17:
    print("good afternoon")
elif hour <21:
    print("good evening")
else:
    print("good night")    