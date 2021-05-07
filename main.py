import random

def solve(comp,you):
    if comp=="r":
        if you=="p" or you=="s":
            return False
        else:
            return None
    if comp=="p":
        if you=="r" or you=="s":
            return True
        else:
            return None
    if comp == "s":
        if you == "r":
            return True
        elif you=="p":
            return False
        else :
            return None


print("Computer's turn to select : Rock(r) or Paper(p) or Scissor(s) ")
comp=random.randint(1,3)
if comp==1:
    comp="r"
elif comp==2:
    comp="p"
else :
    comp="s"
print("Computer selected! ")
print("Your turn to select : Rock(r) or Paper(p) or Scissor(s) ")
you=input()

print("Computer selected "+comp+"\nYou selected "+you+"\nResult time \U0001F604 ")

if(solve(comp,you)==1):
    print("You Win!")
elif solve(comp,you)==0:
    print("Computer Wins!")
else:
    print("Draw!")

