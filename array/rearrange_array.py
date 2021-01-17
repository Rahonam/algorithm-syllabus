
def rearrange_array(arr:list):
    """
    Rearrange the array such that A[i]=i if A[i] exists, otherwise -1

    using: iteration, time O(n) space O(1)

    Args:
        arr: array of integers
    
    Returns:
        array: the rearranged array
    """
    for i in range(0, len(arr) - 1):
        if arr[i] != -1 and arr[i] != i:
            current_element = arr[i]

            while arr[current_element] != -1 and arr[current_element] != current_element:
                arr[current_element], current_element = current_element, arr[current_element]
            
            arr[current_element] = current_element
            if arr[i] != -1:
                arr[i] = -1
    
    return arr


print(rearrange_array([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]))
print(rearrange_array([19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]))