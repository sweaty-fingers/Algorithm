class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        delay = []
        
        for i, t in enumerate(temperatures):
            step = 0

            for j in temperatures[i + 1 :]:

                step += 1

                if j > t:

                    delay.append(step)

                    break

            if len(delay) < i + 1:
                delay.append(0)

        return delay

    ## time out