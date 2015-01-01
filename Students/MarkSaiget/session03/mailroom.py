#! /usr/bin/env python
"""Do Session 3 Homework, Task 3.
“Mail Room”

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
"""


def sendReport():
    """
    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data
    structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Verify that the amount is in fact a number, and re-prompt if it isn’t.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.
    It is fine to forget new donors once the script quits running.
    """


def createReport():
    """
    If the user (you) selected ‘Create a Report’ Print a list of your donors,
    sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations and average donation
    amount as values in each row.
    Using string formatting, format the output rows as nicely as possible. The
    end result should be tabular (values in each column should align with those
    above and below)
    After printing this report, return to the original prompt.
    """


if __name__ == '__main__':

    """A data structure that holds a list of your donors and a history
    of the amounts they have donated. This structure should be populated at
    first with at least five donors, with between 1 and 3 donations each
    """
    donor1 = 'Mark Saiget', 1000.00, 2000.00, 3000.00
    donor2 = 'Raluca Struto', 1000.00
    donor3 = 'Sam Smith', 2000.00, 1000.00
    donor4 = 'Fred Flint', 200.00, 100.00
    donor5 = 'Thelma Holmes', 9000.00
    donors = [donor1, donor2, donor3, donor4, donor5]

    # Prompt to 'Send a Thank You’ or ‘Create a Report’.
    keepGoing = True
    while keepGoing:
        choice = raw_input("Would you like to ‘Send a Thank You’ or ‘Create a \
        Report'?")
        if choice.lower() == 'send a thank you':
            sendReport()
        if choice.lower() == 'create a report':
            createReport
