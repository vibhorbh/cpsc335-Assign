# Names: Vibhor Bhargava, Aly Sayed, Matthew Aaron Gabriel
# Emails: vibhor.b@csu.fullerton.edu, Matthew.Gabriel@csu.fullerton.edu

# Implementation of a solution to the Connecting Pairs of Persons Problem

def return_swaps(row):

    #initialize the variable we intend to return
    number_of_swaps = 0
    # create a copy that we can opperate on without changing the original row
    row_copy = row[:]
    # create a variable to hold what were changing
    hold_value = -1

    #start going through row_copy
    # index variable
    i = 0
    # while loop using index variable going through row_copy
    while i < len(row_copy):
        # check to see if the value is even or odd
        # if even
        if row_copy[i] % 2:
            # check to see if the next number is it's pair
            if row_copy[i] != row_copy[i + 1] + 1:
                # if not a pair, make the value we're searching for the odd number in the pair
                hold_value = row_copy[i] + 1                
                # start looping again to find the number
                for l in range(len(row_copy)):
                    # if we find it, start the replacement process
                    if row_copy[l] == hold_value:
                        # insert the non-pair number
                        row_copy.insert(l, row_copy[i + 1])
                        # then, remove the value we want from list and have hold_value hold it
                        hold_value == row_copy.pop(l + 1)
                        # replace the non-pair number with the correct value
                        row_copy[i + 1] = hold_value
                        # increase number of swaps
                        number_of_swaps += 1
                        # break out of loop
                        break
        # if odd 
        else:
            # check to see if the next number is it's pair
            if row_copy[i] != row_copy[i + 1] - 1:
                # if not a pair, make the value we're searching for the even number in the pair
                hold_value = row_copy[i] - 1             
                # start looping again to find the number
                for l in range(len(row_copy)):
                    # if we find it, start the replacement process
                    if row_copy[l] == hold_value:
                        # insert the non-pair number
                        row_copy.insert(l, row_copy[i + 1])
                        # then, remove the value we want from list and have hold_value hold it
                        hold_value == row_copy.pop(l + 1)
                        # replace the non-pair number with the correct value
                        row_copy[i + 1] = hold_value
                        # increase number of swaps
                        number_of_swaps += 1
                        # break out of loop
                        break
        # either way, move on to next pair
        i += 2
    # finally, return the number of times we performed a swap
    return number_of_swaps
