def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_dict = dict()
    result = []

    # for the lists in the array:
    for lists in arrays:
        # we want to loop through the inner lists
        for nums in lists:
            # see/find all elements that are in each list:
            if nums not in my_dict:
                # add to dict
                my_dict[nums] = 1
            # else: if it is already there:
            else:
                # add +1 since it was in another list
                my_dict[nums] += 1
        
    # then from here we want to check if we have seen a vals:
        # and append any reoccurences in the result arr
        
    for num, count in my_dict.items():
        if count > 1:
            result.append(num)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
