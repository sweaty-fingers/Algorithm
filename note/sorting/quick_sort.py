def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # pivot 보다 큰 요소 찾기
            left += 1
        while right > start and array[right] >= array[pivot]: # pivot 보다 작은 요소 찾기
            right -= 1
        
        if left > right: # 엇갈렸다면 pivot과 작은 요소 교체 (크게 보면 작은요소와 큰 요소 교체)
            array[pivot], array[right] = array[right], array[pivot]
        else: # 엇갈리지 않았다면 작은 요소와 큰 요소 교체
            array[right], array[left] = array[left], array[right]
            
        
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
if __name__ == "__main__":
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print("previous array")
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print("array sorted")
    print(array)                
    
        
        