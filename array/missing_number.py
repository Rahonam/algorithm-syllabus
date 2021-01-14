
def missing_number(arr:list):
    """
    Find the missing number from unsorted consecutive numbers

    using: iteration/sum, sum property time O(n)

    Args:
        arr: array of unsorted consecutive numbers
    
    Returns:
        integer: the missing number from given array
    """
    n = len(arr) + 1
    sum_of_n_consecutive_numbers = int(n * (n + 1)/2)
    return sum_of_n_consecutive_numbers - sum(arr)


def missing_number_xor(arr:list):
    """
    Find the missing number from unsorted consecutive numbers

    using: iteration, XOR property, time O(n)
    Consider    a = a1 ^ a2 ^ a3 ^...^ an
                b = a1 ^ a2 ^ a3 ^...^ an-1
    Then a ^ b = an

    Args:
        arr: array of unsorted consecutive numbers
    
    Returns:
        integer: the missing number from given array
    """
    n = len(arr) + 1

    xor_of_given_numbers = 0
    for i in arr:
        xor_of_given_numbers = xor_of_given_numbers ^ i
    
    xor_of_n_consecutive_numbers = 0
    for i in range(1, n + 1):
        xor_of_n_consecutive_numbers = xor_of_n_consecutive_numbers ^ i

    return xor_of_given_numbers ^ xor_of_n_consecutive_numbers


print(missing_number([1, 2, 4, 5, 6]))
print(missing_number([1, 2, 7, 6, 3, 4]))
print(missing_number_xor([1, 2, 4, 5, 6]))
print(missing_number_xor([1, 2, 7, 6, 3, 4]))