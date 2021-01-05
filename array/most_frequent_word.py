
def most_freq_word(arr: list):
    """
    Find the word in the array which appears the maximum number of times

    using: iteration, map

    Args:
        arr: array of words
    
    Returns:
        str: most frequent word
    """
    word_map = {}
    if len(arr) == 1:
        return arr[0]
    for i in arr:
        if i in word_map:
            word_map[i] += 1
        else:
            word_map[i] = 1
    
    return max(word_map, key=lambda x: word_map[x])

print(most_freq_word(["Algorithms", "String", "Integer", "Integer", "Algorithms", "String", "Integer", "Algorithms", "String", "Algorithms"]))