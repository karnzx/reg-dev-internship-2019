import random
import os
Allowedchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
dir_path = os.path.dirname(os.path.realpath(__file__))
class hangman:
    guess = 10
    score = 0
    wrong_guess = []
    guessed = []
    def __init__(self,category,index,lines):
        self.category = category
        self.index = index
        self.answer = lines[index].split(",")[0]
        self.hint = lines[index].split(",")[1]
        self.List = ["_"]*len(self.answer)

    def printHint(self):
        print("Hint : {}".format(self.hint))
        print()

    def printAnswer(self):
        print(self.answer)

    def update(self):
        for L in range(len(self.List)):
            print(self.List[L],end=" ")
        print("  ",end=" ") # for space :)
        print("score : {}".format(self.score),end=",") 
        print("remaining wrong guess : {}".format(self.guess),end=" ")
        if(self.wrong_guess != []):
            print(",wrong guess : ",end ="")
            for K in range(len(self.wrong_guess)):
                print(self.wrong_guess[K],end=",")
            print()
        else:
            print()
    
    def check(self,Input):
        if(Input.lower() not in [x.lower() for x in self.guessed] or Input.upper() not in [x.upper() for x in self.guessed]):
            self.guessed.append(Input)
            Input = Input.lower()
            if(Input in self.answer):
                for i in range(len(self.answer)):
                    if(Input == self.answer[i]):
                        self.List[i] = Input
                self.score += 10
            else:
                self.score -= 5
                self.guess -= 1
                self.wrong_guess.append(Input)
        else:
            print("already guessed that char")
            

print("""Select Category:
    1).furniture
    2).harware       """)
while(True):
    try:
        category = int(input("category = "))
        if(category < 1 or category > 2):
            print("min category is 1 and max category is 2")
        else:
            break
    except BaseException:
        print("please input number")
    
index = random.randint(0,4)
#print("index = ",index)
if(category == 1):
    path = "\\furniture.txt"
elif(category == 2):
    path = "\\harware.txt"

with open(dir_path + path) as f:
    lines = f.read().splitlines()
    #print(lines)

game = hangman(category,index,lines)
print("Correct( +10 ), wrong(-5 )")
game.printHint()
game.update()
while(True):
    Input = str(input(">guess : "))
    print()
    if(Input in Allowedchars and len(Input) == 1):
        game.check(Input)
        game.update()
    else:
        print("please enter char 1 charcator")
        game.update()
    if(game.guess <= 0):
        print("No more guess")
        print("Score = {}".format(game.score))
        break
    if("_" not in game.List):
        print("guess right!")
        print("Score = {}".format(game.score))
        break