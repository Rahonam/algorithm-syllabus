
def max_subarray(arr: list):
    """
    Find the contiguous subarray within an array of numbers which has the largest sum

    using: iteration, Kadane’s Algorithm, time O(n) space O(1)
    Kadane’s algorithm works only when there is at least one positive element in the array

    Args:
        arr: array of integers
    
    Returns:
        integer: the largest sum of contiguous subarray
    """
    max_so_far = 0
    max_ending_here = 0

    for i in arr:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    
    return max_so_far


def max_subarray_modified(arr: list):
    """
    Find the contiguous subarray within an array of numbers which has the largest sum

    using: iteration, Modified Kadane’s Algorithm, time O(n) space O(1)
    This algorithm works for all negative elements in the array too

    Args:
        arr: array of integers
    
    Returns:
        integer: the largest sum of contiguous subarray
    """
    max_so_far = 0
    max_ending_here = 0

    for i in arr:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


def max_subarray_dp(arr: list):
    """
    Find the contiguous subarray within an array of numbers which has the largest sum

    using: iteration, Dynamic programming, time O(n) space O(n)

    Args:
        arr: array of integers
    
    Returns:
        integer: the largest sum of contiguous subarray
    """
    max_so_far = 0
    solutions = [0] * len(arr)

    for i in range(1, len(arr) -1):
        solutions[i] = max(solutions[i - 1] + arr[i], arr[i])

        if max_so_far < solutions[i]:
            max_so_far = solutions[i]
    
    return max_so_far


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_modified([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_dp([-2, 1, -3, 4, -1, 2, 1, -5, 4]))