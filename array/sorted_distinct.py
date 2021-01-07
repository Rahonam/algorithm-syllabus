
def sorted_distinct(arr: list):
    """
    Find unique elements in the array in sorted order

    using: iteration, dictionary

    Args:
        arr: array of integers
    
    Returns:
        array: sorted distinct elements of array
    """
    arr.sort()
    sorted_map = {}
    for i in arr:
      if i in sorted_map:
        sorted_map[i] += 1
      else:
        sorted_map[i] = 1
    return [i for i in sorted_map.keys()]


print(sorted_distinct( [6, 1, 8, 5, 2, 10, 17, 25, 6, 5, 1, 8, 8]))
print(sorted_distinct([2,2,2,2,2]))