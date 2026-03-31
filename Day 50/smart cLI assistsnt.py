import datetime
# now = datetime.datetime.now()
# print(now.strftime("%D,%m,%Y,%A"))
# print(datetime.datetime.now().strftime())
import webbrowser
# search = input("search youtube")
# webbrowser.open(f"https://www.youtube.com/results?search_query=python tutorial")
while True:
    command = input("Enter command: ").lower()

    if command == "hello":
        print(command)

    elif command == "time":
        print(datetime.datetime.now().strftime("%H:%M:%S")) 

    elif command == "date":
        print(datetime.datetime.now().strftime("%d-%m-%Y"))

    elif command == "day":
        print(datetime.datetime.now().strftime("%A"))

    elif command == "Youtube":
        search = input("search youtube :")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

    elif command == "google":
        search = input("search google")
        webbrowser.open(f"https://www.google.com/search?q={search}")

    elif command == "open youtube":
        webbrowser.open("https://www.youtube.com")            


    elif command == "bye":
        print(command) 

    elif command == "exit":
        break
    else:
        print("unknown command")          