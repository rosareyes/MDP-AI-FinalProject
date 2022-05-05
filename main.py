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
        print(state[0] + cardinal_directions + state[1] + ': ' + str(truncate(probability, 6)) + " ("
              + str(truncate(probability*100, 2)) + "%)")
        # e.g. output:
        # High;High;High;E;High;High;High: 0.616438 (61.64%)


# We define the directions and call the function for each of them.
directions = ['E', 'N', 'W']

for direction in directions:
    transition_tables_probability_counter(direction)





