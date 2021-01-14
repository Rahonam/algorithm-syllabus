
def missing_duplicate(arr:list):
    """
    Find the missing duplicate in a given array

    using: iteration, dictionary, space O(n) time O(n)

    Args:
        arr: array containing duplicates of all the numbers in array except one number
    
    Returns:
        integer: the missing duplicate number from given array
        string: "No missing duplicate", otherwise
    """
    count_map = {}

    for i in arr:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1
    
    for key, value in count_map.items():
        if value == 1:
            return key
    
    return "No missing duplicate"


def missing_duplicate_xor(arr:list):
    """
    Find the missing duplicate in a given array

    using: iteration, XOR property, space O(1) time O(n)
    Consider A^A = 0 and A^B^A = B
    so, XOR all the elements will be the missing duplicate

    Args:
        arr: array containing duplicates of all the numbers in array except one number
    
    Returns:
        integer: the missing duplicate number from given array
        string: "No missing duplicate", otherwise
    """
    xor_of_all_elements = arr[0]

    for i in range(1, len(arr)):
        xor_of_all_elements = xor_of_all_elements ^ arr[i]
    
    if xor_of_all_elements == 0:
        return "No missing duplicate"
    else:
        return xor_of_all_elements


print(missing_duplicate([2,1,3,5,5,3,2,1,6,7,7,8,8]))
print(missing_duplicate([1,1,2,2,3,3,4,4]))
print(missing_duplicate_xor([2,1,3,5,5,3,2,1,6,7,7,8,8]))
print(missing_duplicate_xor([1,1,2,2,3,3,4,4]))