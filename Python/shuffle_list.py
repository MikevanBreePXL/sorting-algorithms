import random
# shuffle algorithmns

# Naïve shuffle: go through every element of the input_list and put it in a random position
def shuffle_naive(input_list):
    for i in range(len(input_list)):
        input_list[random.randint(0, len(input_list)-1)] = input_list[i]

    return input_list

# Fisher-Yates shuffle: Take a random element from the input_list and add it to a seperate (randomized/result) input_list
def shuffle_fischer_yates(input_list):
    result_list = []
    
    for i in range(len(input_list)):
        index = random.randint(0, len(input_list)-1)
        result_list.append(input_list[index])
        input_list.pop(index)
    
    return result_list