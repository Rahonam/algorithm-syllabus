
def contains_range(arr:list, start:int, end:int):
    """
    Check if given array contains all elements of some given range

    using: iteration, time O(n) space O(1)

    Args:
        arr: array of integers
        start: first element of range
        end: last element of range
    
    Returns:
        boolean: True, if array contains all elements of the range
        boolean: False, otherwise
    """
    for i in range(0, len(arr)):
        if start <= arr[i] and arr[i] <= end:
            arr[arr[i] - start] *= -1
    
    for i in range(0, end - start + 1):
        if arr[i] > 0:
            return False
    
    return True


print(contains_range([11, 17, 13, 19, 15, 16, 12, 14], 12, 15))