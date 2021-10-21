class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, value in enumerate(numbers):
            temp = target - value
            if temp in numbers[i+1:]:
                return [i + 1, numbers[i+1:].index(temp) + len(numbers[:i+1]) + 1]



# by 투포인터

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1ㅇ
        
        while left < right: 
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                return [left + 1, right + 1] 


# by 이진 탐색

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, value in enumerate(numbers):
            left = i + 1
            right = len(numbers) - 1
            expect = target - value
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if expect < numbers[mid]:
                    right = mid - 1
                elif expect > numbers[mid]:
                    left = mid + 1
                else:
                    return [i + 1, mid + 1]

# by 이진 탐색 모듈

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, value in enumerate(numbers):
            expect = target - value 
            
            k = bisect.bisect_left(numbers, expect, i+1)
            
            if k < len(numbers) and numbers[k] == expect:
                return [i + 1, k + 1]
            
        