


print ("""You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake. What do you do?")
    print( "1. Take the cake.")
    print ("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print ("The bear eats your face off. Good job!")
    elif bear == "2":
        print( "The bear eats your legs off. Good job!")
    else:
        print( "Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print ("You stare into endless abyss at Cthulhu's retina.")
    print ("1. Blueberries.")
    print( "2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print ("Your body survives powered by a mind of jello. Godd job!")
    else:
        print ("The insanity rots your eyes into a pool of muck. Good job!")

elif door == "3":
    print( "This door is locked with a magical spell. To open it you need to guess a riddle. Do you want to try? yes/no")

    answer = input("> ")

    if answer == "yes":
        print ("'The man who invented it doesn't want it. The man who bought it doesn't need it. The man who needs it doesn't know it'. What is it?")

        riddle_answer = input("> ")


        if riddle_answer == "a coffin":
            print( "Great job! Here's your key. Good luck!")
        else:
            print ("You not thinking hard enough. Try again")

    elif answer == "no":
        print ("You never going to see what's behind this door. Bye!")
    else:
        print ("You need to pick something")

else:
    print ("You stumble around and fall on a knife and die. Good job")
