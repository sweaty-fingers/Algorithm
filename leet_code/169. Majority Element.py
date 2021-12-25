# 풀이 1
## 파이썬의 collecitons.Counter 모듈로 풀이
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = collections.Counter(nums)

        return counter.most_common(1)[0][0] # (요소, 개수) 튜플로 구성된 리스트 형태, [0][0]으로 요소 반환 


# 풀이2
## 분할 정복을 이용


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return None
        elif len(nums) == 1:
            return nums[0]

        a = self.majorityElement(nums[: len(nums) // 2])
        b = self.majorityElement(nums[len(nums) // 2 :])

        return [a, b][nums.count(b) > len(nums) // 2]
