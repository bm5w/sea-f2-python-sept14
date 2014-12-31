#! /usr/bin/env python
"""Do Session 3 Homework, Task 1."""


if __name__ == '__main__':
    """"Perform the tasks below as executable python script."""

    # Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
    aList = [u'Apples', u'Pears', u'Oranges', u'Peaches']

    # Display the list.
    print aList

    # Ask the user for another fruit and add it to the end of the list.
    aList.append(raw_input('Name another fruit to add to list-->').decode('\
        unicode-escape'))
    print aList   # print list

    # Ask the user for a number display the number back to the user and
    # the fruit corresponding to that number (on a 1-is-first basis).
    num = int(raw_input('Input a number-->'))
    print u'Number = {number}\nFruit at index {number} = {fruit}'\
        .format(number=num, fruit=aList[num-1])

    # Add another fruit to the beginning of the list using "+" and display the
    # list.
    aList = [u"Mangos"] + aList
    print aList

    # Add another fruit to the beginning of the list using insert() and display
    # the list.
    aList.insert(0, u"Kiwis")
    print aList

    # Display all the fruits that begin with "P", using a for loop.
    for items in aList:
        if items[0] == u'P':
            print items

    # Using the list created in series 1 above:
    # Display the list.
    aList = [u'Apples', u'Pears', u'Oranges', u'Peaches']
    print aList

    # Remove the last fruit from the list.
    aList.pop()
    print aList

    # Ask the user for a fruit to delete and find it and delete it.
    aList.remove(raw_input('Input a fruit to delete-->').decode('unicode-escape\
        '))

    # (Bonus: Multiply the list times two. Keep asking until a match is found.
    # Once found, delete all occurrences.)
    aList = aList*2
    print aList
    flag = True
    while flag:
        temp = raw_input('Input fruit in list-->')
        while temp in aList[:]:
            aList.remove(temp)
            flag = False
    print aList

    # Again, using the list from series 1:
    # Ask the user for input displaying a line like "Do you like apples?"
    # for each fruit in the list (making the fruit all lowercase).
    # For each "no", delete that fruit from the list.
    # For any answer that is not "yes" or "no", prompt the user to answer with
    # one of those two values (a while loop is good here):
    aList = [u'Apples', u'Pears', u'Oranges', u'Peaches']
    for fruit in aList[:]:
        keepGoing = True
        ans = raw_input("Do you like {fru}?-->".format(fru=fruit.lower())).\
            lower()
        while keepGoing:
            if ans == 'no':
                aList.remove(fruit)
                keepGoing = False
            elif ans == 'yes':
                keepGoing = False
                continue
            else:
                ans = raw_input("Please answer 'yes' or 'no', do you like {fru}?-->\
                    ".format(fru=fruit.lower())).lower()
        print aList
u"""

Display the list.
Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
"""