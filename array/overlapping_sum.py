
def overlapping_sum(arr1: list, arr2: list):
    """
    Sum of all the overlapping elements between two arrays

    using: iteration

    Args:
        arr1: array of integers
        arr2: array of integers
    
    Returns:
        int: sum of overlapping elements of arr1 and arr2
    """
    sum = 0
    arr1_count = {}
    arr2_count = {}

    for i in arr1:
        if i in arr1_count:
            arr1_count[i] += 1
        else:
            arr1_count[i] = 1
    
    for i in arr2:
        if i in arr2_count:
            arr2_count[i] += 1
        else:
            arr2_count[i] = 1
            
    for key, value in arr1_count.items():
        if key in arr2_count:
            min_count = min(value, arr2_count[key])
            sum += key * min_count

    return sum * 2


print(overlapping_sum([6,5,1,9,2,8,3], [3,7,9,2,4]))
print(overlapping_sum([6,5,2,9,2,8,3], [3,2,9,2,4]))
print(overlapping_sum([6,5], [3,7]))