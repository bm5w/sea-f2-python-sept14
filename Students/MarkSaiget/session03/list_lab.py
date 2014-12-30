#!/usr/bin/env python
"""Do Session 3 Homework, Task 1."""


def printList(list):
    for i in list:
        print i

if __name__ == '__main__':
    """"Perform the tasks below as executable python script."""

    # Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
    aList = [u'Apples', u'Pears', u'Oranges', u'Peaches']

    # Display the list.
    printList(aList)

    # Ask the user for another fruit and add it to the end of the list.
    aList.append(raw_input('Name another fruit to add to list-->'))
    printList(aList)    # print list

    """
    Ask the user for a number
    display the number back to the user and
    the fruit corresponding to that number (on a 1-is-first basis).
    """
    num = int(raw_input('Input a number-->'))
    print u'Number = {number}\nFruit at index {number} = {fruit}'\
        .format(number=num, fruit=aList[num-1])

u"""
Add another fruit to the beginning of the list using "+" and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with "P", using a for loop.
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete and find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
Again, using the list from series 1:

Ask the user for input displaying a line like "Do you like apples?"
for each fruit in the list (making the fruit all lowercase).
For each "no", delete that fruit from the list.
For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here):
Display the list.
Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
"""