
def majority_element(arr:list):
    """
    Find the majority element(element appears more than n/2 times) in given array
    Majority Element: If an element appears more than n/2 times in array where n is the size of the array.

    using: iteration, dictionary, time O(n), space O(n)

    Args:
        arr: array of integers
    
    Returns:
        integer: majority element, if exists
        string: "No majority", otherwise
    """
    occurence_map = {}

    for i in arr:
        if i in occurence_map:
            occurence_map[i] += 1
        else:
            occurence_map[i] = 1
    
    max_element = max(occurence_map, key=lambda x: occurence_map[x])

    if max_element > int(len(arr) / 2):
        return max_element
    else:
        return "No majority"


def boyer_moore_majority(arr:list):
    """
    Find the majority element in given array
    Majority Element: If an element appears more than n/2 times in array where n is the size of the array.

    using: iteration, dictionary, Boyer–Moore majority vote algorithm, time O(n), space O(1)
    Boyer-Moore algorithm:  First iteration – Find the candidate element which could be a majority element.
                            Second iteration – check the element(found in first iteration) count is greater than n/2

    Args:
        arr: array of integers
    
    Returns:
        integer: majority element, if exists
        string: "No majority", otherwise
    """
    max_element = arr[0]
    max_element_count = 1
    for i in range(1, len(arr) - 1):
        if arr[i] == max_element:
            max_element_count += 1
        else:
            max_element_count -= 1
        
        if max_element_count == 0:
            max_element = arr[i]
            max_element_count = 1
    
    max_element_count = 0
    for i in arr:
        if i == max_element:
            max_element_count += 1
    
    if max_element_count > int(len(arr) / 2):
        return max_element
    else:
        return "No majority"


print(majority_element([1,3,1,4,1,6]))
print(majority_element([1,3,5,5,5,5,4,1,5]))
print(boyer_moore_majority([1,3,1,4,1,6]))
print(boyer_moore_majority([1,3,5,5,5,5,4,1,5]))