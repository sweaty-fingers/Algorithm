class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Parameters
        -------------
        remain gas : int
        잔존 가스량

        start_node : int
        시작 station의 index
        """

        if sum(gas) < sum(cost):
            return -1


        for j in range(len(gas)):

            if gas[j] - cost[j] < 0 or gas[j] == 0:
                continue

            start_node = j
            remain_gas = gas[j]

            for _ in range(1, len(gas) + 1):
                j = (j + 1) % len(gas)

                remain_gas -= cost[j - 1]

                if remain_gas < 0:
                    break

                remain_gas += gas[j]

                if j == start_node:
                    return j

        return -1


## 한번의 루프로 풀기

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Parameters
        -------------
        start : int
        시작 index, return 값
        
        fuel : 잔존 gas
        """
        
        if sum(gas) < sum(cost):
            return -1
    
        start, fuel = 0, 0
        
        for i in range(len(gas)):
            
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
                
        return start
                
                
                
            
        