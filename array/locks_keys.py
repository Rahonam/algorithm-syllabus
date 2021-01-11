
def match_keys(keys: list, locks: list):
    """
    Find all matches between keys and locks.

    using: iteration, dictionary

    Args:
        keys: array of strings
        locks: array of strings
    
    Returns:
        dictionary: mapping of keys to locks
    """
    key_map = {}

    for i in keys:
        key_map[i] = ""
    
    for i in locks:
        if i in key_map:
            key_map[i] = i
    
    return key_map


print(match_keys(['$', '%', '&', 'x', '@'], ['%', '@', 'x', '$', '&']))