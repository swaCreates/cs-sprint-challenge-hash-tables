def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    my_dict = {}
    
    # create a dict, where the list of weights will be the key
        #dict[key(weights)] = weights[i]
    # and the value of the key would be the index

    # go through the list
    # check if the limit - index has the result in the list
    # if it does return values that sum to the limit
    # if not go to next index
    
    for i, weight in enumerate(weights):
        # print(i, weight)
        if weight not in my_dict:
            my_dict[weight] = i
        else: 
            my_dict[weight] += i

    for i, weight in enumerate(weights):
        weight2 = limit - weight

        # if the result of limit - weight exists in my_dict:
        if weight2 in my_dict:
            # return in an arr the index and key
            indexes_list = [i, my_dict[weight2]]
            # making sure the larger number is before the smaller
            indexes_list.sort(reverse=True)
            return indexes_list

    return None
