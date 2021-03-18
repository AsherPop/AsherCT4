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
        try:
            print("Hello there my friend! Lets get working with lists!")
            print("Choose one of the following options. Type a number ONLY please!")                                                            
            choice = input("""1. Add to list
2. Add a bunch of numbers
3. Return the value at an index position
4. Print contents of list
5. Random Choice
6. Linear Search
7. End Program       """)
            if choice == "1":
                addToList()

            elif choice == "2":
                addABunch()

            elif choice == "3":
                indexValues()

            elif choice == "4":
                print(myList)

            elif choice == "5":
                randomSearch()

            elif choice == "6":
                linearSearch()
               

            else:
                break
        

        except:
            print("An error ocurred when you tried to complete this action")
   


        

def addToList():
    newItem = input("Please type an integer!    ")
    myList.append(int(newItem))
    print(myList)



def addABunch():
    print("We're gonna add a bunch of numbers!!!")
    numToAdd = input("How many integers do you want to add?       ")
    numRange = input("How high would you like these numbers to go?      ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")
        

def indexValues():
    indexPos = input("Which index position would you like to view within your list     ")
    print(myList[int(indexPos)])



def linearSearch():
    print("We're going to search through the list in the worst way possible!")
    searchItem = input("What are you looking for? Number-wise?    ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))




def randomSearch():
    print("Heres a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])




if __name__ == "__main__":
    mainProgram()
