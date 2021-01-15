
def is_consecutive(arr:list):
    """
    Check if all the numbers in the array are consecutive numbers

    using: iteration, dictionary, space O(n) time O(n)

    Args:
        arr: array of unsorted numbers
    
    Returns:
        boolean: True, if all numbers are consecutive
        boolean: False, otherwise
    """
    max_num = max(arr)
    min_num = min(arr)
    
    if len(arr) == (max_num - min_num + 1):
        #check for duplicates
        unique_map = {}
        for i in arr:
            if i in unique_map:
                return False
            else:
                unique_map[i] = ""
    
        return True
    else:
        return False


def is_consecutive_sum(arr:list):
    """
    Check if all the numbers in the array are consecutive numbers

    using: iteration, sum property, space O(1) time O(n)
    S=(n/2)(2a+n-1), S is the sum of n consecutive numbers starting from a

    Args:
        arr: array of unsorted numbers
    
    Returns:
        boolean: True, if all numbers are consecutive
        boolean: False, otherwise
    """
    arr_sum = sum(arr)

    n = len(arr)
    start_num = min(arr)
    n_sum = (n / 2) * ((2 * start_num) + n - 1)
    
    if arr_sum == int(n_sum):
        return True
    else:
        return False


print(is_consecutive([21,24,22,26,23,25]))
print(is_consecutive([11,10,12,14,13]))
print(is_consecutive([11,10,14,13]))
print(is_consecutive([11,10,14,11,11]))
print(is_consecutive_sum([21,24,22,26,23,25]))
print(is_consecutive_sum([11,10,12,14,13]))
print(is_consecutive_sum([11,10,14,13]))
print(is_consecutive_sum([11,10,14,11,11]))