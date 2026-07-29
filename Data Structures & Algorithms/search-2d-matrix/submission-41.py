class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Map rows and columns to indices

        # 0, 0 -> 0 
        # 0, 1 -> 1
        # 0 , 2 -> 2
        # 1, 0 -> 3
        # 1, 1 -> 4
        # 1, 2 -> 5 

        # 1 * 3 -> 3
        # 1 * 3 + 1 -> 4
        # 1 * 3 + 2 -> 5

        # m * n -> N

        # 5 // 3 -> 1 
        # 5 % 3 -> 2 

        rows, cols = len(matrix), len(matrix[0])
        N = rows * cols

        left, right = 0, N-1

        while left <= right:
            mid = left + (right - left) // 2

            row, col = mid // cols, mid % cols
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                left = mid + 1
            
            if matrix[row][col] > target:
                right = mid - 1
        
        return False
