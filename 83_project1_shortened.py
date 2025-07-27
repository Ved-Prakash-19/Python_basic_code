#This logic is written on the basis of computer - you
import random
computer = random.choice([-1,0,1])

youstr = input["enter your choice"]
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}
you = youdict[youstr]
print(f"you choose{reversedict[you]}\ncomputer choose{reversedict[computer]}")

if((comp - you) == -1 or (comp - you) == 2):
    print("Computer wins it means you loose the game!")
else:
    print("You win the game!")
    
    # this is the shortened method of this project after analysis of large and efficient code of this project.