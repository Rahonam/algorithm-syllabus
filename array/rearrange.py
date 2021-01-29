
def rearrange(arr:list):
    """
    Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest, and so on
    
    using: iteration, sorting, time O(log(n)), space O(1)

    Args:
        arr: array of integers
    
    Returns:
    """
    arr.sort() 
    n = len(arr)

    tempArr = [0] * (n + 1) 
    ArrIndex = 0
  
    i = 0
    j = n-1
      
    while(i <= n // 2 or j > n // 2 ) : 
      
        tempArr[ArrIndex] = arr[i] 
        ArrIndex = ArrIndex + 1
        tempArr[ArrIndex] = arr[j] 
        ArrIndex = ArrIndex + 1
        i = i + 1
        j = j - 1
      
    for i in range(0, n) : 
        arr[i] = tempArr[i]

    return arr

print(rearrange([ 5, 8, 1, 4, 2, 9, 3, 7, 6 ] ))