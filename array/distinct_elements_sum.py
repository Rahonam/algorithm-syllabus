
def distinct_sum(arr1: list, arr2: list):
    """
    Find the sum of all elements which are present in either of the given arrays

    using: iteration, dictionary

    Args:
        arr1: array of integers
        arr2: array of integers
    
    Returns:
        int: sum of distinct elements among two given arrays
    """
    sum = 0
    count_map = {}

    for i in arr1:
        if i in count_map:
            count_map[i] += 1
            sum -= i
        else:
            count_map[i] = 1
            sum += i
            
    for i in arr2:
        if i in count_map:
            count_map[i] += 1
            sum -= i
        else:
            count_map[i] = 1
            sum += i

    return sum


print(distinct_sum([3, 1, 7, 9], [2, 4, 1, 9, 3]))