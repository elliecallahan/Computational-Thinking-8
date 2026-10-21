import random 
print (" HI welcome to this marvel themed guessing game")
marvel = input(" Your going to have to guess a marvel charater Ok?")
print("you can quess from the Origanal 6 plus spidey, scarlett witch and dr stange")
print (" Okay lets get started")
mylist = ["Ironman", "Captian america", "Black widow", "Hulk", "Hawkeye", "Thor"," Spiderman", "Scarlett witch", "Dr stange"]
Marvel_hidden = random.choice (mylist)
#print (Marvel_hidden)
#start of for loop 
for i in range(5):
    guess = input("Guess a maverl charater")
    if guess == Marvel_hidden:
        print("You got the charater good work")
        quit()
    else:
        print("oops that not right ")
if guess == Marvel_hidden:
    print (" you got it good job ")
# end of for loop 
print (" I hope this marvel themed guessing game was fun")
print (" Bye")