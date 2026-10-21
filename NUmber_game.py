import random 
hidden_number = random.randint(1,20)
input 

#print (hidden_number)
for i in range (10): 
    guess1 = int(input("guess a number between 1 and 20   "))
    if guess1 == hidden_number:
        print("yay youre right")
    else:
        guess2 = int(input("you are wrong guess again     "))
