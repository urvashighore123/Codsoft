import random as rd

print("Rock-Paper-Scissor Game")

#0 = "rock"
#1 = "paper"
#2 = "scissor"

rock = '''
            _____
     ---- ' _____)
           (_____)
           (____)
     ---.__(___)
     '''
paper = '''
          ____
   -----'  ___)___
          ________)
          _________)
           ________)
    ----' _____)
    '''
scissor = '''
          ____
   -----'  ___)____
          _________)
          _________)
           ____)
    ----' _____)
    '''
game_images = [rock,paper,scissor]

person = int(input("chhose 0 for rock , 1 for paper and 2 for scissor"))
if person>2 or person<0:
    print("you have typed invalid input . you lose")
else:
    print("persons choice is :",person,game_images[person])
    computer = rd.randint(0,2)
    print("computers choice is :",computer,game_images[computer])
    if person==0 and computer==2:
        print("you win!")
    elif computer==0 and person==2:
        print("you lose!")
    elif computer>person:
        print("you lose!")
    elif person>computer:
        print("you win!")
    elif computer==person:
        print("Its a tie!")






