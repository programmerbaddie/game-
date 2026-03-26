import random 
'''
1 for snake 
-1 for water 
0 for gun 
'''
computer = random.choice([-1, 1, 0])
youstr = input("enter your choice:").lower()
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}

if youstr not in youdict:
    print("Invalid choice. Please enter s, w, or g.")
    exit()

you = youdict[youstr]

# now we have 2 number. you and computer 

print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer ]}")


if(computer==you):
    print("its draw")

else:
    if (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
        print("you win")
    else:
        print("you lose")