
def separate_odd_even(arr:list):
    """
    Separate even and odd numbers in given array.

    using: iteration

    Args:
        arr: array of integers
    
    Returns:
        array: array having odd and even numbers separated
    """
    left_index = 0
    right_index = len(arr) - 1

    while left_index < right_index:
        if arr[left_index] % 2 == 0:
            left_index += 1
            continue

        if arr[right_index] % 2 != 0:
            right_index -= 1
            continue
        
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    
    return arr


print(separate_odd_even([1,2,3,4,5,6,7,8]))
print(separate_odd_even([4,1,6,8,7,2,3,12]))