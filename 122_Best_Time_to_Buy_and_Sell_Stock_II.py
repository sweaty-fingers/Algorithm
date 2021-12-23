class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Parameters
        ------------
        prices : List[int]
        가격 정보
        
        having : int
        현재 가지고 있는 주식
        
        current : int
        현재 시점의 주식 가격
        
        total_benefit : int
        총 이익
        
        """    
    
        having = prices[0]
        total_benefit = 0
        
        for current in prices:
            
            if current - having > 0:
                total_benefit += current - having
                
                having = current
                
            if current - having < 0:
                having = current
                
        
        return total_benefit
                