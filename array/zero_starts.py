
def zero_starts(arr:list):
    """
    Find the index from which 0 starts in the given array

    using: iteration, time O(n)

    Args:
        arr: array of 1s followed by 0s
    
    Returns:
        integer: index of first 0, if exists
        string: "No zeros", otherwise
    """
    index = -1
    for i in range(0, len(arr) - 1):
        if arr[i] == 0:
            index = i
            break
    if index > -1:
        return index
    else:
        return "No zeros"


def zero_starts_binary_search(arr:list, end_index: int, start_index: int = 0):
    """
    Find the index from which 0 starts in the given array

    using: iteration, time O(log n)

    Args:
        arr: array of 1s followed by 0s
        end_index: index of last element
        start_index: index of first element
    
    Returns:
        integer: index of first 0, if exists
        string: "No zeros", otherwise
    """
    if start_index == end_index:
        if arr[start_index] == 0:
            return start_index
        else:
            return "No zeros"
    else:
        mid = int((start_index + end_index) / 2)
        if arr[mid] == 0 and arr[mid - 1] == 1:
            return mid
        
        if arr[mid] == 0 and arr[mid - 1] == 0:
            return zero_starts_binary_search(arr, start_index, mid - 1)
        
        if arr[mid] == 1:
            return zero_starts_binary_search(arr, mid + 1, end_index)


print(zero_starts([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]))
print(zero_starts([0,0,0,0,0,0,0]))
print(zero_starts([1,1,1,1,1,1,1,1,1,1]))
print(zero_starts_binary_search([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0], 16))
print(zero_starts_binary_search([0,0,0,0,0,0,0], 6))
print(zero_starts_binary_search([1,1,1,1,1,1,1,1,1,1], 9))