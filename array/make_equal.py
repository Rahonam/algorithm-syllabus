
def make_equal(arr:list, step:int):
    """
    Find the number of operations needed to make all elements of array equal. Where a single operation can increment an element by given step
    
    using: iteration, time O(n), space O(1)

    Args:
        arr: array of integers
        step: increment step for one operation
    
    Returns:
        integer: number of operation, if possible to make all elements equal
        integer: -1, otherwise
    """
    operations = 0
    max_num = max(arr)

    for i in arr:
        if (max_num - i) % step != 0:
            return -1
        else:
            operations += (max_num - i) // step
    
    return operations


print(make_equal([4, 7, 19, 16], 3))
print(make_equal([4, 4, 4, 4], 3))
print(make_equal([4, 2, 6, 8], 3))