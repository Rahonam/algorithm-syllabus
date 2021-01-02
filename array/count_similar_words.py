
def similar_words(arr: list):
    """
    Count similar words in a given array 

    using: iteration, dictionary

    Args:
        number: array of strings
    
    Returns:
        dict: a map of string to its occurence
    """
    word_map = {}
    for i in arr:
        i = i.replace(" ", "")
        i = i.lower()
        if i in word_map:
            word_map[i] = word_map[i] + 1
        else:
            word_map[i] = 1

    return word_map

print(similar_words(['apple', 'Apple', 'apple ', 'cat', 'CAT', 'bat']))
print(similar_words(['apple', 'Apple', 'apple ', 'cat', 'CAT', 'bat']))