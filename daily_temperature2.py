class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        delay = [0] * len(temperatures)
        idx_stack = []
        temp_stack = []

        for i, t in enumerate(temperatures):

            while idx_stack and t > temp_stack[-1]:
                temp_stack.pop()
                ans_idx = idx_stack.pop()
                delay[ans_idx] = i - ans_idx

            idx_stack.append(i)
            temp_stack.append(t)

        return delay
