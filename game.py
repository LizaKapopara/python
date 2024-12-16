import random

n = random.choice([-1, 0, 1])
ls = ["s","w","g"]
print(ls)
yourstr = str(input("Enter your choice from above list:"))
yourDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"Gun"}

you = yourDict[yourstr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[n]}")

if(n == you):
    print("It's a draw")
elif(n == -1 and you == -1):
    print("you win")
elif(n == -1 and you ==0):
    print("you lose")
elif(n == 1 and you == -1):
   print("you lose")
elif(n == 1 and you == 0):
    print("you win")
elif(n == 0 and you == -1):
    print("you win")
elif(n == 0 and you == 1):
    print("you lose")