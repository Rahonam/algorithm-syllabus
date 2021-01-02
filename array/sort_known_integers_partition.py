
def sort_integers(arr: list):
    """
    Sort 0’s, the 1’s and 2’s in the given array – Dutch National Flag algorithm | Set – 2

    using: iteration, inplace

    Args:
        number: array of integers, that consists only of three types of integers, which are 0, 1 and 2
    
    Returns:
        array: sorted array
    """
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr


print(sort_integers([2,1,2,0,1,0]))
print(sort_integers([0, 0, 2, 0, 2, 1, 0, 1, 2]))