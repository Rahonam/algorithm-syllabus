
def subset_sums(arr: list, index: int = 0, sum: int = 0):
    """
    Find all the sum of subsets individually

    using: recursion

    Args:
        arr: array of integers
        index: current index to start traversing from
        sum: sum of current subset
    
    Returns:
        
    """
    if index > len(arr) - 1:
        print(sum, end=" ")
        return
    
    subset_sums(arr, index + 1, sum + arr[index])

    subset_sums(arr, index + 1, sum)


print(subset_sums([1, 2]))
print(subset_sums([2, 4, 6]))