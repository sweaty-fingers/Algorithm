def bisect_right(array: list, target: str, start=0, end=None):
    
    if not end:
        end = len(array)
        
    while start < end:
        mid = start + (end - start) // 2
        
        if array[mid] > target:
            end = mid
        else:
            start = mid + 1

    return start