
def odd_xor(arr: list):
    """
    Find the number of pairs with odd XOR 

    For bits:
        XOR is 0 if same bits, otherwise 1

    using: iteration

    Args:
        arr: array of integers
    
    Returns:
        int: count of odd XOR pairs
    """
    if len(arr) == 1:
        return 0

    count = 0
    left_index = 0
    while left_index < len(arr) - 1:
        right_index = left_index + 1
        while right_index < len(arr):
            xor = (arr[left_index] | arr[right_index]) & (~arr[left_index] | ~arr[right_index])
            xor = (arr[left_index] | arr[right_index]) & (~arr[left_index] | ~arr[right_index])
            if xor % 2 != 0:
                count += 1
            right_index += 1
        left_index += 1

    return count


def oddXor(arr: list):
    """
    Find the number of pairs with odd XOR 

    For bits:
        XOR is 0 if same bits, otherwise 1

    For numbers:
        XOR is odd if one number is odd and another is even, otherwise even

    using: iteration

    Args:
        arr: array of integers
    
    Returns:
        int: count of odd XOR pairs
    """
    if len(arr) == 1:
        return 0

    odd_count = 0
    even_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count * even_count


print(oddXor([3]))
print(oddXor([3,2,1]))
print(oddXor([3,6,9,4]))