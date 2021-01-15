
def sum_closest_to_zero(arr:list):
    """
    Find the two elements such that, their sum is closest to zero.

    using: iteration, sorting, space O(1) time O(nlog(n))

    Args:
        arr: array of integers
    
    Returns:
        array: two elements whose sum is closest to zero
    """
    if len(arr) < 3:
        return arr

    arr.sort()

    n = len(arr) - 1
    i = 0

    num1, num2 = arr[i], arr[n]
    closest = arr[n] + arr[n - 1]
    while i < n:
        if arr[i] + arr[n] == 0:
            return [arr[i], arr[n]]
        elif arr[i] + arr[n] > 0:
            n -= 1
            if arr[i] + arr[n] < closest:
                num1, num2 = arr[i], arr[n]
        else:
            i += 1
            if arr[i] + arr[n] > closest:
                num1, num2 = arr[i], arr[n]

    return [num1, num2]


print(sum_closest_to_zero([1, 4, -5, 3, -2, 10, -6, 20]))
print(sum_closest_to_zero([-5,5,8]))
print(sum_closest_to_zero([5,8]))
print(sum_closest_to_zero([-5,5,-8]))