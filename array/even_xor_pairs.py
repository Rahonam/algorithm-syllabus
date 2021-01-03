
def evenXor(arr: list):
    """
    Find the number of pairs with even XOR 

    For bits:
        XOR is 0 if same bits, otherwise 1

    For numbers:
        XOR is odd if one number is odd and another is even, otherwise even

    using: iteration

    Args:
        arr: array of integers
    
    Returns:
        int: count of even XOR pairs
    """
    if len(arr) == 1:
        return 1

    odd_count = 0
    even_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return int((odd_count * (odd_count - 1) / 2) + (even_count * (even_count - 1) / 2))


print(evenXor([3]))
print(evenXor([3,2,1]))
print(evenXor([3,6,9,4]))