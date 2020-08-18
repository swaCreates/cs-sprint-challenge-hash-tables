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
    # if not go to next index
    for i, weight in enumerate(weights):
        # print(i, weight)
        if weight not in my_dict:
            my_dict[weight] = i
        if limit - my_dict[weight] == limit:
            return my_dict[weights[i]]
        else:
            i += 1
    return None
