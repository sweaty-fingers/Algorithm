# Time out error

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        i = 0
        max_window = []
        
        while i <= len(nums)-k:
            
            max_window.append(max(nums[i:i+k]))
            i += 1
            
        return max_window
            
        


# Timeout error
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        current_max = float('-inf')
        max_windows = []
        
        window = deque()
        
        for i, n in enumerate(nums):
            
            window.append(n)
            
            if i < k - 1:
                continue
                
            if current_max == float('-inf'):
                current_max = max(window)
            elif n > current_max:
                current_max = n
                
            max_windows.append(current_max)
            
            if window.popleft() == current_max:
                current_max = float('-inf')
        
        return max_windows


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q_idx = deque()
        results = []
        
        l_b_idx = 0 # left boundary index
        r_b_idx = 0 # right boundary index
        
        while r_b_idx < len(nums):
            
            while q_idx and nums[q_idx[-1]] < nums[r_b_idx]:
                q_idx.pop()
                
            q_idx.append(r_b_idx)
            
            
            if l_b_idx > q_idx[0]:
                q_idx.popleft()
                
            
            if r_b_idx >= k - 1:
                
                results.append(nums[q_idx[0]])
                
                l_b_idx += 1
            
            r_b_idx += 1
            
        return results
                
                                                   
                
            