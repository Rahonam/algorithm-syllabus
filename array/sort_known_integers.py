
def sort_integers(arr: list):
    """
    Sort 0’s, the 1’s, and 2’s in the given array. | Set – 1

    using: iteration, counting

    Args:
        number: array of integers, that consists only of three types of integers, which are 0, 1 and 2
    
    Returns:
        array: sorted array
    """
    zeros = 0
    ones = 0
    twos = 0

    for i in arr:
        if i == 0:
            zeros += 1
        if i == 1:
            ones += 1
        if i == 2:
            twos += 1
    
    for i in range(zeros):
        arr[i] = 0
    
    for i in range(zeros, zeros + ones):
        arr[i] = 1
    
    for i in range(zeros + ones, len(arr)):
        arr[i] = 2
    
    return arr


print(sort_integers([2,1,2,0,1,0]))
print(sort_integers([0, 0, 2, 0, 2, 1, 0, 1, 2]))