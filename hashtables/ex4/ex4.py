def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # loop through list
    # store integers as key
    # find corresponding ints and increment count +1
    # return result of ints > 1

    my_dict = {}
    count = 0

    for nums in a:
        my_dict[nums] = a[nums]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
