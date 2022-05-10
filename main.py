import csv
import itertools
import math

"""
MARKOV DECISION PROCESS (MDP) - FINAL PROJECT
---------------------------------------------
SUBJECT:        ARTIFICIAL INTELLIGENCE

AUTHORS:        100434072 - ROSA REYES
                100451104 - INES SANZ
"""

# First, we define the two lists with the combinations for the transition tables of our MDP
list_1 = ['High;High;High;', 'High;High;Low;', 'High;Low;High;', 'High;Low;Low;', 'Low;High;High;',
          'Low;High;Low;', 'Low;Low;High;', 'Low;Low;Low;']
list_2 = [';High;High;High', ';High;High;Low', ';High;Low;High', ';High;Low;Low', ';Low;High;High',
          ';Low;High;Low', ';Low;Low;High', ';Low;Low;Low']

# Then, we do a cartesian product to obtain all the possible combinations
all_states_combinations = list(itertools.product(list_1, list_2))

print("<-----------MARKOV DECISION PROCESS MODEL------------>")
print("States: N(High/Low), E(High/Low), W(High/Low)")
print("Actions:")
print("Turn_green_north()")
print("Turn_green_east()")
print("Turn_green_west()")
print("All possible combinations for states:", all_states_combinations)  # len: 64 possible combinations
# rows defined to save all the .csv data
rows = []

# reading the csv file
with open('data/Data.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names for first row
    fields = next(csvreader)

    # extracting each data row by row
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total nr. of rows with header: %d" % csvreader.line_num)

# printing the field names
print('Field names are:\n' + ', '.join(field for field in fields))


def truncate(number, digits) -> float:
    """Helper function to truncate probabilities"""
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def transition_tables_probability_counter(cardinal_directions):
    directions_dictionary = {}
    """Function to calculate all the probabilities for the transition table"""
    print("Transition table for %s:\n" % cardinal_directions)
    # for every possible combination
    for state in all_states_combinations:
        total_cases = 0

        # we iterate the rows with the data
        for r in rows:
            # for every row in our transition tables, we count all the occurrences
            # of it to calculate the probabilities
            # e.g. first row for green light in east 'E': H;H;H;E -> we count the rows and save it
            if (state[0] + cardinal_directions) in r[0]:
                total_cases = total_cases + 1
        # some combinations do not appear in data.csv, so they'd be 0.
        if total_cases != 0:
            # calculate the probability for every cell dividing it by the total cases for each row
            probability = rows.count([state[0] + cardinal_directions + state[1]]) / total_cases
        else:
            probability = 0
        directions_dictionary[state[0] + cardinal_directions + state[1]] = str(truncate(probability, 6))
        print(state[0] + cardinal_directions + state[1] + ': ' + str(truncate(probability, 6)) + " ("
              + str(truncate(probability*100, 2)) + "%)")
        # e.g. output:
        # High;High;High;E;High;High;High: 0.616438 (61.64%)
    return directions_dictionary


# We define the directions and call the function for each of them
directions = ['E', 'N', 'W']
# We save the data in dictionaries for each direction
dictionaries = []

for direction in directions:
    dictionaries.append(transition_tables_probability_counter(direction))




# we separate each dictionary into a different variable
#dictionary_1 = dictionaries[0] # contains probabilities of table action E
#dictionary_2 = dictionaries[1] # contains probabilities of table action N
#dictionary_3 = dictionaries[2] # contains probabilities of table action W

# We calculate the cost of action E in all the bellman equations for all 8 states

# Calcular el ExpC_E (que se usara luego para calcular las bellman equations
# result_cost_E = 0
# i = 0
# iteration = 1
# state = 'High;High;High;'


def calculate_cost_east(state, iteration, state_value_list):
    cost_east = 1
    result_cost_east = 0
    i = 0
    for item in dictionaries[0]:
        if state in item:

            #print("i", i)
            result_cost_east = result_cost_east + float(dictionaries[0][item])*state_value_list[i][iteration-1]
            #print("dictionaries[0][item]",dictionaries[0][item])

            i = i+1
    Exp_cost_east = cost_east + result_cost_east
    #print("Exp_cost_east", Exp_cost_east )
    # print("resultadooooo", Exp_cost_east)
    return Exp_cost_east


def calculate_cost_north(state, iteration, state_value_list):
    cost_north = 1
    result_cost_north = 0
    i = 0
    for item in dictionaries[1]:
        if state in item:
            #print("I AM IN NORTH")
            #print("STATE", state)
            #print("iteration", iteration)
            #print("i", i)
            result_cost_north = result_cost_north + float(dictionaries[1][item])*state_value_list[i][iteration-1]
            #print("dictionaries[0][item]", dictionaries[1][item])
            #print("state_value_list[i][iteration-1]", state_value_list[i][iteration - 1])
            #print("result_cost_east ", result_cost_north)
            i = i+1
    Exp_cost_north = cost_north + result_cost_north
    #print("Exp_cost_north", Exp_cost_north)
    # print("resultadooooo", Exp_cost_north)
    return Exp_cost_north


def calculate_cost_west(state, iteration, state_value_list):
    cost_west = 1
    result_cost_west = 0
    i = 0
    for item in dictionaries[2]:
        if state in item:
            #print("I AM IN WEST")
            #print("STATE", state)
            #print("iteration", iteration)
            #print("i", i)
            result_cost_west = result_cost_west + float(dictionaries[2][item])*state_value_list[i][iteration-1]
            #print("dictionaries[0][item]", dictionaries[2][item])
            #print("state_value_list[i][iteration-1]", state_value_list[i][iteration - 1])
            #print("result_cost_east ", result_cost_west)
            i = i+1
    Exp_cost_west = cost_west + result_cost_west
    #print("Exp_cost_west", Exp_cost_west)
    return Exp_cost_west


state_value_list = [[0], [0], [0], [0], [0], [0], [0], [0]]

#cost_for_east= calculate_cost_east('High;High;High;', 1, state_value_list)
#cost_for_north = calculate_cost_north('High;High;High;', 1, state_value_list)
#cost_for_west= calculate_cost_west('High;High;High;', 1, state_value_list)
#bellman_eq_for_hhh= min(cost_for_west, cost_for_north, cost_for_east)


def bellman_equations(state, iteration, state_value_list):
    cost_E = calculate_cost_east(state, iteration, state_value_list)
    cost_N = calculate_cost_north(state, iteration, state_value_list)
    cost_W = calculate_cost_west(state, iteration, state_value_list)

    bellman_eq = round(min(cost_E, cost_W, cost_N),2)
    if state == 'High;High;High;':
        state_value_list[0].append(bellman_eq)
        #print("HE ENTRADO EN 1, resultado states_list", state_value_list)
    elif state == 'High;High;Low;':
        state_value_list[1].append(bellman_eq)
        #print("HE ENTRADO EN 2, resultado states_list", state_value_list)
    elif state == 'High;Low;High;':
        state_value_list[2].append(bellman_eq)
        #print("HE ENTRADO EN 3, resultado states_list", state_value_list)
    elif state == 'High;Low;Low;':
        state_value_list[3].append(bellman_eq)
        #print("HE ENTRADO EN 4, resultado states_list",state_value_list)
    elif state == 'Low;High;High;':
        state_value_list[4].append(bellman_eq)
        #print("HE ENTRADO EN 5, resultado states_list", state_value_list)
    elif state == 'Low;High;Low;':
        state_value_list[5].append(bellman_eq)
        #print("HE ENTRADO EN 6, resultado states_list", state_value_list)
    elif state == 'Low;Low;High;':
        state_value_list[6].append(bellman_eq)
        #print("HE ENTRADO EN 7, resultado states_list", state_value_list)
    elif state == 'Low;Low;Low;':
        state_value_list[7].append(bellman_eq)
        #print("HE ENTRADO EN 8, resultado states_list", state_value_list)

    return state_value_list

# preguntar cuantos decimales tomar en cuenta
for number in range(1,120):
    #print("num", number)
    for state in list_1:
        bellman_equations(state, number, state_value_list)


#print("RESULTADOOOOOOO", state_value_list)

for elemento in state_value_list:
    print(elemento)
