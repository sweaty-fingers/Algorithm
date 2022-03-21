class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            left = 0
            right = len(row) - 1
            
            while left <= right:
                
                mid = left + (right - left) // 2
                
                if target < row[mid]:
                    right = mid - 1
                elif target > row[mid]:
                    left = mid + 1
                else:
                    return True
         
    
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= (len(matrix) - 1) and col >= 0:
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            
            
        return False



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


