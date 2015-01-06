#! /usr/bin/env python
"""Do Session 4 Homework, updating mailroom.py
"Mail Room"

Write a small command-line script called mailroom.py. As with Task 1, This
script should be executable. The script should accomplish the following goals:

At any point, the user should be able to quit their current task and return to
the original prompt.
From the original prompt, the user should be able to quit the script cleanly
First, factor your script into separate functions. Each of the above tasks can
be accomplished by a series of steps. Write discreet functions that accomplish
individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use-case for the while loop.

Put the functions you write into the script at the top.

Put your main interaction into an if __name__ == '__main__' block.

UPDATES:
use dicts where appropriate
write a full set of letters to everyone to individual files on disk
see if you can use a dict to switch between the users selections
Try to use a dict and the .format() method to do the letter as one big template
rather than building up a big string in parts.
"""
import os
import io


def totalD(donor):
    """Given donor history (name followed by donation amounts) return total"""
    return sum(donors[donor])


def addDonor(name):
    """Add donor name to database"""
    donors[name.title()] = []


def sendReport():
    """If the user (you) selects 'Send a Thank You', provide note."""
    """
    If the user types 'list', show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data
    structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Verify that the amount is in fact a number, and re-prompt if it isn't.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.
    It is fine to forget new donors once the script quits running.
    """
    going = True
    while going:
        # Prompt for full name.
        fullName = raw_input("Please provide a full name in (First Last)"
                             " format or type 'list' for a list of donor names"
                             "-->").lower()
        if fullName == "quit":
            going = False
            break
        elif fullName == "list":
            print donors.keys()
            break
        else:
            if fullName in donors:
                break
            else:
                # add name to data structure
                addDonor(fullName)
            keep = True
            while keep:
                amt = raw_input("Enter donation amount-->")
                # Verify amt is number
                if amt == "quit":
                    keep = False
                    going = False
                    break
                # Verify is numeric and only one decimal
                try:
                    amt = float(amt)
                    # add amt to donation history
                    donors[fullName.title()].append(amt)
                    # Print Letter
                    print """Dear {name}, \nThank you for your generous donation of ${amount}.\n\tSincerely,\n\tMark Saiget""".\
                        format(name=fullName.title(), amount=amt)
                    createLetters()
                    keep = False
                    going = False
                except ValueError:
                    print u"Input must be float, try again."


def createLetters():
    """write a full set of letters to everyone to individual files on disk"""
    link = os.getcwd() + '/' + 'letters' + '/'
    try:
        print link
        os.mkdir(link)
    except OSError:
        print "Path already exists."
    for key, value in donors.iteritems():
        outfile = io.open(link + '/' + key + '.txt', 'w')
        text = u"""Dear {name}, \nThank you for your generous donation of ${amount}.\n\tSincerely,\n\tMark Saiget""".\
            format(name=key.title(), amount=sum(donors[key]))
        outfile.write(text)
        outfile.close()


def createReport():
    """Create report with historical donation information"""
    """
    If the user (you) selected 'Create a Report' Print a list of your donors,
    sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations and average donation
    amount as values in each row.
    Using string formatting, format the output rows as nicely as possible. The
    end result should be tabular (values in each column should align with those
    above and below)
    After printing this report, return to the original prompt.
    """
    # Get order sorted by total historical donation amount
    donorsSort = donors.keys()
    donorsSort.sort(key=totalD)
    # Print Report
    print "DONOR NAME\tTOTAL\t\tNUMBER OF DONATIONS\tAVERAGE DONATION"
    for donor in donorsSort:
        total = sum(donors[donor])
        number = len(donors[donor])
        print "{name}\t{total}\t\t{number}\t\t\t{avg}".format(
            name=donor, total=total, number=number, avg=total/number)


if __name__ == '__main__':
    """A data structure that holds a list of your donors and a history
    of the amounts they have donated. This structure should be populated at
    first with at least five donors, with between 1 and 3 donations each
    """
    donors = {}
    donors['Thelma Holmes'] = [9000.00]
    donors['Mark Saiget'] = [1000.00, 2000.00, 3000.00]
    donors['Raluca Struto'] = [1000.00]
    donors['Sam Smith'] = [2000.00, 1000.00]
    donors['Fred Flint'] = [200.00, 100.00]

    # Prompt to 'Send a Thank You' or 'Create a Report'.
    keepGoing = True
    options = {'1': sendReport, '2': createReport}
    while keepGoing:
        choice = raw_input("Would you like to:\n1)  Send a Thank You\n"
                           "2)  Create a Report\n"
                           "3)  Quit\n"
                           "Input '1', '2', or '3'-->")
        try:
            options[choice]()
        except (KeyError, TypeError):
            print "Please enter a valid input value."
        finally:
            if choice == '3':
                keepGoing = False
