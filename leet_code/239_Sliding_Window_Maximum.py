# Time out error

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        i = 0
        max_window = []
        
        while i <= len(nums)-k:
            
            max_window.append(max(nums[i:i+k]))
            i += 1
            
        return max_window
            
            
            
            