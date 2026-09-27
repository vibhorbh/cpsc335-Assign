# Names: Vibhor Bhargava, Aly Sayed, Matthew Aaron Gabriel
# Emails: vibhor.b@csu.fullerton.edu, Matthew.Gabriel@csu.fullerton.edu

# Implementation of a Selection sory solution to the Connecting Pairs of Persons Problem

def return_swaps(row):

    #initialize the variable we intend to return
    number_of_swaps = 0
    # create a copy that we can opperate on without changing the original row
    row_copy = row[:]
    # create a variable to hold the sorted row
    sorted_row = []
    # create a variable to hold what were changing
    hold_value = -1

    #start going through row_copy
    # index variable
    i = 0
    # while loop using index variable going through row_copy
    while i < len(row_copy):
        # check to see if there is a pair
        if row_copy[i] != row_copy[i + 1] - 1 or row_copy[i] != row_copy[i + 1] + 1:
            # when there is no pair, start looking for the pair to row_copy[i] then swap them
            if row_copy[i] % 2:
                hold_value = row_copy[i] + 1
            else:
                hold_value = row_copy[i] - 1
            for l in range(len(row_copy)):
                if 






    # finally, return the number of times we performed a swap
    return number_of_swaps