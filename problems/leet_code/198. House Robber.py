#리스트 인덱스를 한칸씩 이동하면서 값을 누적하면서 풀기
##1. 두칸 전 누적 값 + 현재 노드의 돈 > 이전 노드의 누적 값 ? 두칸 전 누적 값 + 현재 노드의 돈 : 이전 노드의 누적 값
##2. 첫 번째와 두번 째 노드는 별도 처리
##3. 리스트 길이가 2이하 경우 두 요소 중 최대 값 반환

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: # 리스트 길이가 2 이하 경우 두 요소 중 최대 값 반환
            return max(nums)
        
        if nums[0] > nums[1]: # 첫 번째와 두번 째 노드는 별도 처리
            nums[1] = nums[0]
        
        for i in range(2, len(nums)): 두칸 전 누적 값 + 현재 노드의 돈 > 이전 노드의 누적 값 ? 두칸 전 누적 값 + 현재 노드의 돈 : 이전 노드의 누적 값
            if nums[i] + nums[i - 2] < nums[i - 1]:
                nums[i] = nums[i - 1]
            else:
                nums[i] = nums[i] + nums[i - 2]
            
        
        return nums[-1] # 누적 최대 값이 들어있을 마지막 노드 반환


# max 함수를 이용해서 다음과 같이 if ~ else문을 간단하게 표현할 수 있음.

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        if nums[0] > nums[1]:
            nums[1] = nums[0]
        
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i -2], nums[i - 1])        
        
        return nums[-1]