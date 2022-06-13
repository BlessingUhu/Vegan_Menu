# greet user and welcome them to the page

# user should choose their meal for the day.

# create different files for breakfast, lunch and dinner and snack (access each file using a for loop)

# ask user if they would like to start over. If no, quit the program.

'''(to be continued. Later Project) once user inputs breakfast, lunch or dinner, the program
should present a recipe including a general idea of the quantity needed for each ingredient e.g (ibs, tbs, Tbs, etc)
 and also things they need to buy for that specific meal. Later on, direct links will be placed on where user can buy
those ingredients if they are unavailable. (Most of these done using Javascript, etc)
'''

import random

# main variables
bt = ""  # breakfast string holder
lt = ""  # lunch string holder
dt = ""  # dinner string holder
st = ""  # snacks string holder
bList = list()  # breakfast array
lList = list()  # lunch array
dList = list()  # dinner array
sList = list()  # snacks array
bcount = 0  # counting how many meals in each file for breakfast
lcount = 0  # counting how many meals in each file for lunch
dcount = 0  # counting how many meals in each file for dinner
scount = 0  # counting how many meals in each file for dinner
v = ""  # sentence determiner (an & a)

greeting = input("Hello and welcome to Biomestom! Please enter your name: ")

greetingAns = input(
    "Hi " + greeting + "! " + "What would like to eat today? Please enter 'breakfast', 'lunch' or 'dinner.' " + "\n")

while True:

    myMeal = greetingAns.lower()

    if "breakfast" in myMeal:
        # breakfast files

        bFile = open("breakfast.txt")
        for meals in bFile:
            bt = meals + bt
            bt = bt.strip()
            bList = bt.split("\n")
            bcount += 1

        # taking random breakfast meals

        r = random.randint(0, bcount)

        # collecting vowel sounds to make sentence clear
        vowels = set("aeiouAEIOU")

        for vowel in vowels:
            if bList[r].startswith(vowel):
                v = "an"
            else:
                v = "a"

        print("Here is a suggested breakfast meal! Try making", v, bList[r], "\n")

    elif "lunch" in myMeal:
        # opening lunch txt files

        lFile = open("lunch.txt")
        for meals in lFile:
            lt = lt + meals
            lList = lt.split("\n")
            lcount += 1

        # taking random lunch meals

        r = random.randint(0, lcount)

        # collecting vowel sounds to make sentence clear
        vowels = set("aeiouAEIOU")

        for vowel in vowels:
            if lList[r].startswith(vowel):
                v = "an"
            else:
                v = "a"

        print("Here is a suggested lunch meal! Try making", v, lList[r], "\n")

    elif "dinner" in myMeal:
        # opening dinner txt files

        dFile = open("dinner.txt")
        for meals in dFile:
            dt = dt + meals
            dList = dt.split("\n")
            dcount += 1

        # taking random lunch meals

        r = random.randint(0, dcount)

        # collecting vowel sounds to make sentence clear
        vowels = set("aeiouAEIOU")

        for vowel in vowels:
            if dList[r].startswith(vowel):
                v = "an"
            else:
                v = "a"

        print("Here is a suggested dinner meal! Try making", v, dList[r], "\n")

    else:
        print("Incorrect answer")
        greetingAns = input("Please enter 'breakfast', 'lunch' or 'dinner.' ")
        continue

    # snacks
    ques = input("I hope you enjoy the meal! How about some nutritious snacks afterwards? Do you want know what I "
                 "have in mind? Enter 'yes' or 'no' to exit")
    sResponse = ques.lower()

    if "yes" in sResponse:
        sFile = open("snacks.txt")
        for snacks in sFile:
            st = st + snacks
            sList = st.split("\n")
            scount += 1

        # taking random lunch meals

        r = random.randint(0, scount)

        # collecting vowel sounds to make sentence clear
        vowels = set("aeiouAEIOU")

        for vowel in vowels:
            if sList[r].startswith(vowel):
                v = "an"
            else:
                v = "a"

        print("Here you go! Try", v, sList[r], "\n")

        #  starting program over again

        a = input("Would like to start over? ")
        startOver = a.lower()

        if "yes" in startOver:
            greetingAns = input("What would like to eat today? Please enter 'breakfast', 'lunch' or 'dinner'")
            continue
        else:
            print("See you again soon at Biomestom!")
            break
    else:
        print("Alright, you have a great day and hope to see you again soon at Biomestom!")
        break

exit()
