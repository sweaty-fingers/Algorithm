class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for i in nums:
            output = output ^ i
        
        return output
            

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        exist = set(nums)
        for i in exist:
            nums.remove(i)
        
        return (exist - set(nums)).pop()
            