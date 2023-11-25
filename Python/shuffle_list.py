import random
# shuffle algorithmns

# Naïve shuffle: go through every element of the list and put it in a random position
def shuffle_naive(list):
    for i in range(len(list)):
        list[random.randint(0, len(list)-1)] = list[i]

    return list

# Fisher-Yates shuffle: Take a random element from the list and add it to a seperate (randomized/result) list
def shuffle_fischer_yates(list):
    result_list = []
    
    iteration_length = len(list)
    for i in range(iteration_length):
        result_list.append(list[random.randint(0, len(list)-1)])
    
    return result_list