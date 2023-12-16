# cost_E = 1
prob_state = ' '
state_value_list = [[0],[0],[0],[0],[0],[0],[0],[0]] # here we will save the state values of the succesive iterations
                                                     # of each of the states(1-8)
# we declare the variables of the result of the sumatory of the probabilities * the sate values
result_HHH_E = 0
result_HHL_E = 0
result_HLH_E = 0
result_HLL_E = 0
result_LHL_E = 0
result_LHH_E = 0
result_LLH_E = 0
result_LLL_E = 0


# with the for loop we go through all the probabilities of action E table and add them in their corresponding states
# for item in dictionary_1:
    if prob_state == 'High;High;High;':
        result_HHH_E = result_HHH_E + float(dictionary_1[item])*state_value_list[0][i-1]

    if prob_state == 'High;High;Low;':
        result_HHL_E = result_HHL_E + float(dictionary_1[item])*state_value_list[1][i-1]

    if prob_state == 'High;Low;High;':
        result_HLH_E = result_HLH_E + float(dictionary_1[item])*state_value_list[2][i-1]

    if prob_state == 'High;Low;Low;':
        result_HLL_E = result_HLL_E + float(dictionary_1[item])*state_value_list[3][i-1]

    if prob_state == 'Low;High;High;':
        result_LHH_E = result_LHH_E + float(dictionary_1[item])*state_value_list[4][i-1]

    if prob_state == 'Low;High;Low;':
        result_LHL_E = result_LHL_E + float(dictionary_1[item])*state_value_list[5][i-1]

    if prob_state == 'Low;Low;High;':
        result_LLH_E = result_LLH_E + float(dictionary_1[item])*state_value_list[6][i-1]

    if prob_state == 'Low;Low;Low;':
        result_LLL_E = result_LLL_E + float(dictionary_1[item])*state_value_list[7][i-1]

ExpC_HHH_E = cost_E + result_HHH_E
ExpC_HHL_E = cost_E + result_HHL_E
ExpC_HLH_E = cost_E + result_HLH_E
ExpC_HLL_E = cost_E + result_HLL_E
ExpC_LHH_E = cost_E + result_LHH_E
ExpC_LHL_E = cost_E + result_LHL_E
ExpC_LLL_E = cost_E + result_LLL_E

print("Cost of E in state HHH first iteration", ExpC_HHH_E)
