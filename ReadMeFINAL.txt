Section 1:
How to use the program

Steps:
1. Run the program
2. Use either the "add a bunch of numbers" function or the "add to list function" located on the main menu to add numbers to the list. 
Use the "add a bunch of numbers" function for the code to work better.
3. After you have added numbers to the list, use the function "sort the list" to create a new list that is in order and has no excess numbers. 
This will allow you to use other functions because the original list will not work with the binary searches.
4. Use one of the binary search functions to search for a value in the sorted list. 
5. You can use any of the other functions after you search for a value, such as the "clear list" function if you would like to restart without 
ending the program. You can also use the "view the lists" function if you would like to view your entire list without searching through them.
6. To exit the program, simply finish the function you are in, return to the main menu, and use the option, "End program".

Both the unsorted and sorted lists are needed for this program, without the sorted list, you will not be able to complete some of the functions
in the program, and the unsorted list is less complex, and harder to understand.
If you do not follow these instructions, you will get errors in the program, causing the program to return to main menu, 
or even end in some cases.


Section 2:
The binary search algorithms

	The Binary Search functions work by taking the sorted list(because it is in order from the lowest to highest value) and finding the middle
point in the list. It then locates which half of the list your value is located in, and searches through that half until it locates which index
position the value you searched for is at.
	The recursive binary search function determines which half of the list the value you searched for is in. After it determines what half of the list
your value is on, it calls itself back into its own function, causing the search to loop until it finds your value, allowing it to search the entire
list. However, because it is calling itself back in its own function, this can cause the recursive search to get stuck in an infinite loop, that it
can never get out of and can cause either the program or your computer to crash.
	The iterative binary search is very similar, however instead of setting a midpoint and searching outwards, it searches from the low and high points
until it gets to the midpoint, which is your value! This works similarly to finding a median in math. You cut off the high and low points until you
get to a middle point, where the function then spits our your value at its index position.


Section 3:
Changes that can be made to this program

	This program, despite being very cool and functional, is pretty messy. For example, every single time you want to use a function, it simply
returns you to a large main menu where you have to select an option from the list of functions. When you choose one of these functions, it 
runs fine unless you mess it up and force an error. However, this main menu definetely gets pretty boring. So, instead of just having one, very large 
menu, we could add a sort of choose your own adventure type of program, where if you select a certain function in a certain order, it will get you
to another menu that has more complex options that are based off of the functions your previously chose. This new menu will also contain an option
to get back to the main menu, where you will be able to clear the program and restart without having to end and restart the program as a whole.
This improvement will be very good for the user because it will no longer be chaotic at the start menu, and the amount of values and functions listed 
on the different menus.
	

