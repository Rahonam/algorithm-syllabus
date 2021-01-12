
def triplet_sum_zero(arr:list):
    """
    Find three elements in an array that sum to a zero

    using: iteration, dictionary

    Args:
        arr: array of integers
    
    Returns:
        arr: array of three elements that sum to a zero
    """
    triplet = [0,0,0]
    difference_map = {}

    for i in arr:
        difference_map[1] = ""
    
    for element in arr:
        for i in arr:
            if i == element:
                continue
            if -(i + element) in difference_map:
                triplet[0] = element
                triplet[1] = i
                triplet[2] = -(i + element)
            else:
                difference_map[i] = ""

    return triplet


print(triplet_sum_zero([ 3,-1,-7,-4,-5,9,10]))
print(triplet_sum_zero([-4,-5,9]))