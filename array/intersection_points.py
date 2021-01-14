
def intersection_points(arr1:list, arr2:list):
    """
    Find intersection points between two sorted arrays

    using: iteration, dictionary, space O(n) time O(n)
            this method works with unsorted arrays too

    Args:
        arr1: array of sorted numbers
        arr2: array of sorted numbers
    
    Returns:
        array: intersection points between given arrays
    """
    common_numbers = []

    unique_map = {}
    for i in arr1:
        if i in unique_map:
            return False
        else:
            unique_map[i] = ""
    for i in arr2:
        if i in unique_map:
            common_numbers.append(i)
    
    return common_numbers


def intersection_points_compare(arr1:list, arr2:list):
    """
    Find intersection points between two sorted arrays

    using: iteration, space O(1) time O(n)
            this method works with sorted arrays only

    Args:
        arr1: array of sorted numbers
        arr2: array of sorted numbers
    
    Returns:
        array: intersection points between given arrays
    """
    common_numbers = []

    len1 = len(arr1)
    len2 = len(arr2)
    while len1 and len2:
        if arr1[len1 - 1] == arr2[len2 - 1]:
            common_numbers.append(arr1[len1 - 1])
        if arr1[len1 - 1] > arr2[len2 - 1]:
            len1 -= 1
        else:
            len2 -= 1
    
    return common_numbers


print(intersection_points([1,2,3,6,8,10], [4,5,6,11,15,20]))
print(intersection_points([1,2,3,6,8,10], [2,4,5,6,11,15]))
print(intersection_points_compare([1,2,3,6,8,10], [4,5,6,11,15,20]))
print(intersection_points_compare([1,2,3,6,8,10], [2,4,5,6,11,15]))