import random

def game():
    print("you are playing the game")
    score = random.randint(1,60)
    
    # fetch the high score:-
    with open("92_hiscore.txt") as f:
        hiscore = f.read()
        
        if(hiscore != ""):
            hiscore = int(hiscore)       #f.read karte hai to string ke form me aata hai. so i convert string to integer form. int(hiscore)
        else:
            hiscore = 0
            
    print(f"your score:{score}")  #or print("your score:" + str(score))  # Without f-strings.
    # Why Use f-strings?
    # Readability: It's easier to read and write than concatenating strings and variables.
    if(score>hiscore):
        # write the hiscore to the file
        with open("92_hiscore.txt","w") as f:
            f.write(str(score))
            
    return score

game()
