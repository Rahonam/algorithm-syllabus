
def subsets_sum(arr: list):
    """
    Find sum of the sums of all possible subsets

    using: iteration, occurence of an element in any subset is 2^n-1

    Args:
        arr: array of integers
    
    Returns:
        integer: sum of subsets sum
    """
    sum = 0
    distribution = pow(2, len(arr) - 1)

    for i in arr:
        sum += i * distribution
    
    return sum


print(subsets_sum([]))
print(subsets_sum([3]))
print(subsets_sum([3, 7]))
print(subsets_sum([10, 16, 14, 9]))