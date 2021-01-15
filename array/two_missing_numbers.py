
from functools import reduce
import math

def two_missing_numbers(arr:list):
    """
    Find two missing numbers from unsorted consecutive numbers

    using: iteration/sum, sum property time O(n)

    Args:
        arr: array of unsorted consecutive numbers
    
    Returns:
        array: two missing numbers from given array
    """
    n = max(arr)

    sum_of_arr = sum(arr)
    sum_of_n_consecutive_numbers = int(n * (n + 1)/2)

    product_of_arr = reduce(lambda x,y: x * y, arr)
    product_of_n_consecutive_numbers = reduce(lambda x,y: x * y, [i for i in range(1, n + 1)])
    
    sum_of_missing_numbers = sum_of_n_consecutive_numbers - sum_of_arr
    product_of_missing_numbers = product_of_n_consecutive_numbers // product_of_arr

    d = math.sqrt((sum_of_missing_numbers*sum_of_missing_numbers) - (4*product_of_missing_numbers))
    num1 = int(sum_of_missing_numbers + d)//2

    return [num1, sum_of_missing_numbers - num1]


print(two_missing_numbers([10,2,3,5,7,8,9,1]))