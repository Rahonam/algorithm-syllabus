
def duplicate_numbers(arr: list):
    """
    Find duplicates in the given array

    using: iteration, map, time O(n) space O(n)

    Args:
        arr: array of integers
    
    Returns:
        array: the duplicate numbers
    """
    number_map = {}
    duplicate_numbers = []
    for i in arr:
        if i in number_map:
            if i not in duplicate_numbers:
                duplicate_numbers.append(i)
        else:
            number_map[i] = ""
    
    return duplicate_numbers


def duplicate_numbers_const_space(arr: list):
    """
    Find duplicates in the given array

    using: iteration, map, time O(n) space O(1)
    This solution works only if 
    1. array has positive integers and 
    2. all the elements in the array are in range from 0 to n-1, where n is the size of the array.

    Args:
        arr: array of integers
    
    Returns:
        array: the duplicate numbers
    """
    number_map = {}
    duplicate_numbers = []
    for i in arr:
        if arr[i - 1] < 0:
            if -1 * arr[i - 1] not in duplicate_numbers:
                duplicate_numbers.append(-1 * arr[i - 1])
        else:
            arr[i - 1] *= -1
    
    return duplicate_numbers


print(duplicate_numbers([4, 6, 2, 1, 2, 5]))
print(duplicate_numbers([1, 2, 6, 5, 2, 3, 3, 2]))
print(duplicate_numbers_const_space([4, 6, 2, 1, 2, 5]))
print(duplicate_numbers_const_space([1, 2, 6, 5, 2, 3, 3, 2]))