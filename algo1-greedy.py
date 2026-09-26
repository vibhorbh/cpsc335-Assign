# Names: Vibhor Bhargava, Aly Sayed, Matthew Aaron Gabriel
# Emails: vibhor.b@csu.fullerton.edu,

#Implementation of a greedy algorithm to solve the Hamiltonian Problem

def preferred_starting_city(distance, fuel, mpg):

    starting_position = 0
    curr_point = 0


    for i in range(len(distance)):
        # In this step, we take the current point and add it to fuel times mpg to find how much we can travel on current fuel amount.
        # In the next step, we subtract distance to next city from the current point so we can get distance needed to be travelled.
        curr_point += fuel[i] * mpg
        curr_point -= distance[i]
        
        # If we run out of gas, we can't start from current city, so we have to use next city as the starting point
        if curr_point < 0:
            starting_position = i + 1
            curr_point = 0 # reset our tank for the next stretch

    #and to end the search, we return the current starting point or city
    return starting_position

distance = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Run the function and print the answer
print(preferred_starting_city(distance, fuel, mpg))