started=False
gear_1=False
while True:
    command=input('>').lower()
    if command=="help":
        print ("""
        'start' to start the car
        'stop' to stop the car
        'quit' to quit the game
        '1,2,3,4,5 to change gear
        select manual or automatic gear'""")
    elif command=='start':
        if started:
            print ("the car is already started")
        else:
            started=True
            print("the car is started")
    elif command=='stop':
        if not started:
            print ("the car is already stopped")
        else:
            print ("the car is stopped")
            started=False
    elif command=="1":
        if not started:
            print ("First please start the car")
        else:
            print ("Car gear is set at 1")
            gear_1=True
    elif command=="2":
        if not gear_1:
            print ("please shift first to gear 1")
        elif not started:
            print ("please start the car first")
        else:   
            print ("Car gear is set at 2")
    elif command=="3":
        if not gear_1:
            print ("please shift first to gear 1")
        elif not started:
            print ("please start the car first")
        else:
            print ("Car gear is set at 3")
    elif command=="4":
        if not gear_1:
            print ("please shift first to gear 1")
        elif not started:
            print ("please start the car first")
        else:
            print ("Car gear is set at 4")
    elif command=="5":
        if not gear_1:
            print ("please shift it first to gear 1")
        elif not started:
            print ("please start the car first")
        else:
            print ("Car gear is set at 5")
    elif command=='quit':
        break
    else:
        print ("Sorry but i didn't understand that")
