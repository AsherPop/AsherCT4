"""
program goals:
-get input from user
-conver input into INT
-add that input into a list
-pull values from specific index positions\
"""

#create functions that perform those actions above
import random

myList = []


def mainProgram():
    while True:
        
        print("Hello there my friend! Lets get working with lists!")
        print("Choose one of the following options. Type a number ONLY please!")
        choice = input("""1. Add to list
2. Return the value at an index position
3. End Program       """)
        if choice == "1":
            addToList()

        elif choice == "2":
            indexValues

        elif choice == "3":
            break
    #need to add way to exit the program and catch errors made by the user


        

def addToList():
    newItem = input("Please type an integer!    ")
    myList.append(int(newItem))
    print(myList)

    

def indexValues():
    indexPos = input("Which index position would you like to view within your list     ")
    print(myList[int(indexPos)])



def randomSearch():
    print("Heres a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])




if __name__ == "__main__":
    mainProgram()
