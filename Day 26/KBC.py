question = [
    "India ki capital kya hai?",
    "Python kis cheez ke liye use hota hai?"
]

option = [
    ["1. Mumbai", "2. Delhi", "3. Kolkata", "4. Chennai"],
    ["1. Games", "2. Website", "3. Programming", "4. Music"]
]

answers = [2, 3]
prize = [150, 15]

money = 0

for i in range(len(question)):
    print("\n", question[i])

    for opt in option[i]:
        print(opt)

    ans = int(input("Answer 1-4 likho: "))

    if ans == answers[i]:
        money = prize[i]
        print("Sahi jawab ✅", money)
    else:
        print("Galat jawab ❌")
        break   # ✅ ab ye loop ke andar hai

print("\nGame over")
print("Total money:", money)
