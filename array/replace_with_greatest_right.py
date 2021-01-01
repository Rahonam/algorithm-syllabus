
def replace_greatest(arr: list):
    """
    Replace Elements with Greatest Element on Right 

    using: 

    Args:
        arr: an array of integers
    
    Returns:
        array: array after replacing each element with greatest on its right
    """
    if len(arr) == 1:
        return arr
    
    left_index = len(arr) - 2
    while left_index > -1:
        if arr[left_index] < arr[left_index + 1]:
            arr[left_index] = arr[left_index + 1]
        left_index -= 1

    return arr

print(replace_greatest([4]))
print(replace_greatest([4,5,2,25,13,16,8]))
print(replace_greatest([4,5,2,25,13,16,38]))

