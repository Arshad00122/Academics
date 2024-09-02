#Guess game

Secret_number=9
count=0
guess_limit=2
while count<=guess_limit:
    guess=int(input("Guess: "))
    count+=1
    if guess==Secret_number:
        print ("Hurray! you won the game. ")
        break
    else:
        print ("No not the correct answer. ")
else:
    print ("Sorry (;_;) but you failed.")
