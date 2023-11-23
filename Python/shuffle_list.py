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

sorted_list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(shuffle_naive(sorted_list))
print(shuffle_fischer_yates(sorted_list))