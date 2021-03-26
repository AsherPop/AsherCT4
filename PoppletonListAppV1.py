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
unique_list = []
jokes = ["A bear walks into a bar and says, 'Give me a whiskey and … cola.' 'Why the big pause?' asks the bartender. The bear shrugged. 'I’m not sure; I was born with them.'"]


def mainProgram():
    while True:
        try:
            print("Hello there my friend! Lets get working with lists!")
            print("Choose one of the following options. Type a number ONLY please!")                                                            
            choice = input("""1. Add to list
2. Add a bunch of numbers
3. Return the value at an index position
4. Sort the list
5. View the list(sorted or unsorted)
6. Random Choice
7. Linear Search
8. Funny Joke(You gotta trust me)
9. End Program       """)
            if choice == "1":
                addToList()

            elif choice == "2":
                addABunch()

            elif choice == "3":
                indexValues()

            elif choice == "4":
                sortList(myList)

            elif choice == "5":
                printLists()

            elif choice == "6":
                randomSearch()

            elif choice == "7":
                linearSearch()

            elif choice == "8":
                funnyJoke()
               

            else:
                break
        

        except:
            print("An error ocurred when you tried to complete this action")
   


        

def addToList():
    newItem = input("Please type an integer!    ")
    myList.append(int(newItem))
    print(myList)




def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("You wanna see your new list? y/n     ")
    if showMe.lower() == "y":
        print(unique_list)




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



def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Oh, what luck! Your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, low + 1, high, x)
    else:
        print("Your number isn't here!")


        

"""
def viewList():
    listView = input("Your list could be very long, are you sure you want to view it without sorting first? y/n     ")
    if listView == "y":
        print(myList)

    else:
        print("Alright choose the sorting option this time!!!")
"""  
        
    

def randomSearch():
    print("Heres a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])



def funnyJoke():
    goodJoke = input("Would you really like to hear a joke? y/n    ")
    if goodJoke == "y":
        print(joke)
        

    else:
        print("Ok then, it is very funny though!")



def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichList = input("Which list? Sorted or unsorted?")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)




if __name__ == "__main__":
    mainProgram()
