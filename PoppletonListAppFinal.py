"""
program goals:
-get input from user
-conver input into INT
-add that input into a list
-pull values from specific index positions\
"""


import random

myList = []
unique_list = []
joke = ("A bear walks into a bar and says, 'Give me a whiskey and ....... cola.' 'Why the big pause?' asks the bartender. The bear shrugged. 'I’m not sure; I was born with them.'")

#The main menu of the program which calls functions we built in our code when a user selects a certain option. The main menu gets called to in every function so that we return to it when a function either malfunctions or ends.
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
9. Recursive Binary Search
10. Iterative Binary Search
11. Clear the Lists
12. End Program       """)
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

            elif choice == "9":
                binSearch = input("What number are you looking for?    ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))

            elif choice == "10":
                binSearch = input("What number are you looking for?    ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number is not found in that list you silly goose!")

            elif choice == "11":
                clearList()

            else:
                break
        

        except:
            print("An error ocurred when you tried to complete this action")
   


#This function asks the user which number they want to add to the list, but is very ineffective because it only adds one at a time        
def addToList():
    newItem = input("Please type an integer!    ")
    myList.append(int(newItem))
    print(myList)



#This function asks the user if they want to clear the list, and which list they want to clear, it then clears that list and returns them to the menu.
def clearList():
    clearList = input("Would you like to clear the list(there are a lot of numbers)? Yes or no?    ")
    if clearList == "yes":
        whichList = input("Which list would you like to clear? Sorted, unsorted, or both?     ")
        if whichList == "sorted":
            myList.clear()
            print("Your unsorted list has been cleared!")
        elif whichList == "unsorted":
            unique_list.clear()
            print("Your sorted list has been cleared!")
        elif whichList == "both":
            unique_list.clear()
            myList.clear()
            print("Both of your lists have been cleared!")
        else:
            return
    else:
        print("Alright, I won't clear the lists.")
            
            

#This function ask the user if they want to sort the list, and if so, then it removes any number doubles and rearranges the numbers in numerical order in a new list called unique_list.    
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("You wanna see your new list? y/n     ")
    if showMe.lower() == "y":
        print(unique_list)



#This function is a more complex way to add numbers to  the list, and you can choose how many numbers you want and how big the numbers you want are going to go.
def addABunch():
    print("We're gonna add a bunch of numbers!!!")
    numToAdd = input("How many integers do you want to add?       ")
    numRange = input("How high would you like these numbers to go?      ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")
        

#This function asks you which index position you would like to view in the list, and gives you the number at that index postition.
def indexValues():
    indexPos = input("Which index position would you like to view within your list     ")
    print(myList[int(indexPos)])


#This function searches for a specific number in the list, and goes from lowest to highest in the random list which takes a very long time and is inefficient.
def linearSearch():
    print("We're going to search through the list in the worst way possible!")
    searchItem = input("What are you looking for? Number-wise?    ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))


#This function searches through the sorted list, which is very effective, and splits the list in 2 to see where your number is.
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



#This is very similar to the recursive search, however instead of setting things equal to x, it sets things less than and greater than x,
#so it splits the list in half and the middle number that is in between the high and low point is the mid point which is used in the search to find your number.
def interativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1
            
    


#This function randomly spits out a number from the list when selected.
def randomSearch():
    print("Heres a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])


#This function prints a joke to the user to add a bit of user friendliness into the program.
def funnyJoke():
    goodJoke = input("Would you really like to hear a joke? y/n    ")
    if goodJoke == "y":
        print(joke)
        

    else:
        print("Ok then, it is very funny though!")


#This function does exaclty as it says, it simply prints the list that you want to see.
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichList = input("Which list? Sorted or unsorted?")
        if whichList.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)




if __name__ == "__main__":
    mainProgram()
