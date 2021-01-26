def gcd(a:int, b:int):
    """
    Find the Greatest common divisor of given numbers

    using: recursion, Euclidean algorithm, time O(log(n)) n = min(a,b)

    Args:
        a: integer
        b: integer
    
    Returns:
        integer: gcd of a and b
    """
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a > b:
        return gcd(a % b, b)
    elif b > a:
        return gcd(a, b % a)
    else:
        return a


def rotate(arr:list, d:int):
    """
    Rotate the given array by d elements 

    using: iteration, time O(n*d) space O(1)

    Args:
        arr: array of integers
        d: number of elements to rotate
    
    Returns:
        array: the rotated array
    """
    n = len(arr)
    set_size = max(d % n, gcd(n, d % n))

    for size in range(set_size):
        i = size
        temp = arr[i]
        
        while i + set_size < n:
            arr[i] = arr[i + set_size]
            i += set_size
        arr[size - set_size] = temp
    
    return arr


print(rotate([1, 2, 3, 4, 5, 6, 7], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3))