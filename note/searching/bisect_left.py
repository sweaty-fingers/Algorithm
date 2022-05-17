def bisect_left(array: list, target: str, start=0, end=None):
    if not end:
        end = len(array)
    
    while start < end:
        mid = start + (end - start) // 2
        
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid
            
    return start