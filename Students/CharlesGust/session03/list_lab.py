#!/usr/bin/python


def series1(alist):
    """ print fruit lists and searches from session03, series 1 """
    alist = ["Apples", "Pears", "Oranges", "Peaches"]
    print alist

    another_fruit = raw_input("What's another fruit?-->")
    alist.append(another_fruit)
    print alist

    anumber = raw_input("What's a number?-->")
    if int(anumber) > 0 and int(anumber) < len(alist):
        print alist[int(anumber)-1]

    alist = ["Tomato"] + alist
    print alist

    alist.insert(0, "Avocado")
    print alist

    for i in alist:
        if i[0] == "P":
            print i

    return alist


def series2(alist):
    """ print fruit lists and simple list manipulation from session03, series2 """

    s2_list = alist[:]
    print s2_list

    s2_list = s2_list[:-1]
    print s2_list

    fruit_to_delete = raw_input("Fruit to delete?")
    for fruit in s2_list:
        if fruit == fruit_to_delete:
            s2_list.remove(fruit_to_delete)

    """ the instructions do not say to print the list at this time but it would
        be senseless to perform the list manipulation and not display that it
        occurred
        """
    print s2_list
    return s2_list


def series2a(alist):
    """ print fruit lists and delete multiple occurences without 'set' """
    s2_list = alist[:]
    s2_list *= 2
    print s2_list

    s2_list_static = s2_list[:]
    ask_delete = True
    while ask_delete:
        fruit_to_delete = raw_input("Fruit to delete?")

        for fruit in s2_list_static:
            if fruit == fruit_to_delete:
                ask_delete = False
                s2_list.remove(fruit_to_delete)
    print s2_list
    return s2_list


def series3(alist):
    """ print fruit list after asking user if they like each fruit and delete the ones not liked in seesion03, series3"""
    new_list = []
    for fruit in alist:
        ask_like = True
        while ask_like:
            like_fruit = raw_input("Do you like %s? (yes/no):" % fruit.lower())
            if like_fruit == "no":
                ask_like = False
            elif like_fruit == "yes":
                new_list.append(fruit)
                ask_like = False
    print new_list
    return new_list


def series4(alist):
    """ print fruit lists after reversing characters and removing first element from original """
    alist_copy = []
    for fruit in alist:
        """ using selector [::-1] to reverse a string was shown in class """
        alist_copy.append(fruit[::-1])

    """ instructions say to "Delete last item of the original list"
        but are ambiguous as to whether this item should be deleted
        from the original list, or the copy with reversed letters, so
        this ambiguity is resolved in favor of manipulating the original
        list. If the other meaning is intended, the clause "in the copy"
        should be added after the instruction.
    """
    alist_original = alist[:-1]

    """ instructions say to "Display the original list" but both lists
        have in fact been modified and neither is original.
    """
    print alist_original
    print alist_copy


if __name__ == "__main__":
    alist = []
    alist = series1(alist)
    series2(alist)
    series2a(alist)
    series3(alist)
    series4(alist)
