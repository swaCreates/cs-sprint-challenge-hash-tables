def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # UPER
    # loop through list
    # store integers as key
    # find corresponding ints and increment count +1
    # return result of ints > 1

    my_dict = {}
    result = []

    for num in a:
        if abs(num) not in my_dict:
            my_dict[abs(num)] = 1
        else:        
            my_dict[abs(num)] += 1
        
    for num, count in my_dict.items():
        if count > 1:
            result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
