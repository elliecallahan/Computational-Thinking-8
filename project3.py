#veriablies satrt at 0 
birthday_points = 0 
halloween_points = 0
christmas_points = 0 

answer1 = input("What do you like better A ballons, B Pumpkins, or C candy canes")
if answer1 == "A" or answer1 == "a":
    birthday_points += 1
elif answer1 == "B" or answer1 == "b":
    halloween_points += 1
elif answer1 == "C" or  answer1 =="c":
    christmas_points += 1 

answer2 = input("What do you like better A rainbow , B orange, purple and black , or C red green and white")
if answer2 == "A" or answer2 == "a":
    birthday_points += 1
elif answer2 == "B" or answer2 == "b":
    halloween_points += 1
elif answer2 == "C" or answer2 == "c":
    christmas_points += 1   

answer3 = input(" do you like A Cake, B Pumpkin pie , or C ginderbread")
if answer3 == "A" or answer3 == "a":
    birthday_points += 1
elif answer3 == "B" or answer3 =="b":
    halloween_points += 1
elif answer3 == "C" or answer3 == "c":
    christmas_points += 1   

answer4 = input("What do you like better A  Gifts or B dressing up")
if answer4 == "A" or answer4 == "a":
    birthday_points += 1
    christmas_points += 1
elif answer4 == "B" or answer4 == "b":
    halloween_points += 1

answer5 = input(" Whats your favorite smell  A cupcakes , B pumkin and apples  , or C snow and christmas trees")
if answer5 == "A" or answer5 == "a":
     birthday_points += 1
if answer5 == "B" or answer5 == "b" :
     halloween_points += 1
elif answer5 == "C" or answer5 == "c":
     christmas_points += 1   
     #showing the score of the veriables 
     
print(f" The score you got is {birthday_points} birthday, {halloween_points} halloween, and {christmas_points} Christmas")
# telling you you if your more birthday, halloween, or christmas

if birthday_points > halloween_points and birthday_points > christmas_points: 
    print ("You are a birthday person, you like fun colorful things and are probely really cheerful")
    #If the points Are manily A than it will be Birthday
if halloween_points > birthday_points and halloween_points >christmas_points: 
    print("You are Hallween. your a little spooky but you also love fall and relxing")
    #if anwsers/points are mainly B than you will get Halloween 
if christmas_points > birthday_points and christmas_points > halloween_points: 
    print(" You are christmas. You like cozy days and love to winter and feeling jolly. ")
    #if awnsers are mainly C than youll get Christmas
