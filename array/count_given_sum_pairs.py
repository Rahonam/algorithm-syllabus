
def sum_pairs(arr: list, sum: int):
    """
    Count the number of pairs with a given sum

    using: iteration, dictionary

    Args:
        arr: array of integers
        sum: target sum of pairs
    
    Returns:
        int: count of possible pairs
    """
    pair_count = 0
    count_map = {}
    for i in arr:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1
            
    for key, value in count_map.items():
        if (sum - key) in count_map:
            count1 = value
            count2 = count_map[sum - key]
            if count1 == count2 and count1 > 1:
                pair_count += int(count1 * (count1 - 1) / 2)
            else:
                pair_count += count1 * count2
            count_map[key] = 0
            count_map[sum - key] = 0

    return pair_count

print(sum_pairs([4, 5, 1, 2, 9, -2, -4],5))
print(sum_pairs([1, 5, 7, 1, -1],6))
print(sum_pairs([3, 3, 3, 3],6))