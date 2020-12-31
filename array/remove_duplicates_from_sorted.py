
def remove_duplicates(arr: list):
    """
    Remove Duplicates from Sorted Array 

    using: 

    Args:
        arr: an array of integers
    
    Returns:
        array: sorted array having distinct integers
    """
    if abs(arr[-1] - arr[0]) == len(arr) - 1:
        print("direct")
        return arr

    left_index = 0
    right_index = 1
    while right_index < len(arr):
        if arr[left_index] != arr[right_index]:
            arr[left_index+1] = arr[right_index]
            left_index += 1
            right_index += 1
        else:
            right_index += 1
    
    return arr[:left_index+1]

print(remove_duplicates([1]))
print(remove_duplicates([1,2,3]))
print(remove_duplicates([1,2,3,3,4,4]))
print(remove_duplicates([-1,0,2,3,4]))
print(remove_duplicates([-1,0,2,3,3,4,4]))
print(remove_duplicates([-3,-2,-1]))
print(remove_duplicates([-4,-4,-3,-3,-2,-1]))
print(remove_duplicates([3,2,1]))
print(remove_duplicates([4,4,3,3,2,1]))