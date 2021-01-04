
def common_prefix(p: str):
    """
    Find The Longest Sequence Of Prefix Shared By All The Words In A String

    using: iteration

    Args:
        p: string containing multiple words
    
    Returns:
        str: common prefix
    """
    arr = p.split(" ")
    index = 0
    for i in range(1, len(arr)):
        while index < len(arr[0]) and index < len(arr[i]) and arr[0][index] == arr[i][index]:
            index += 1

    return arr[0][:index]


print(common_prefix("bedroom bedclock bedtable bedwall"))
print(common_prefix("goodluck goodmorning, goodwill"))