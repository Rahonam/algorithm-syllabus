
def smallest_impossible_sum(arr:list):
    """
    Find the smallest number that cannot be formed by the sum of any subsets of sorted array

    using: iteration, space O(1) time O(n)

    Args:
        arr: array of sorted numbers
    
    Returns:
        integer: the smallest impossible sum of any subsets
    """
    smallest_sum = 1
    for i in arr:
        if i > smallest_sum:
            return smallest_sum
        else:
            smallest_sum += i

    return smallest_sum


print(smallest_impossible_sum([1,1,3,4,6,7,9]))
print(smallest_impossible_sum([1,1,1,1,1]))
print(smallest_impossible_sum([2,3,6,7]))
print(smallest_impossible_sum([1,2,6,7,9]))