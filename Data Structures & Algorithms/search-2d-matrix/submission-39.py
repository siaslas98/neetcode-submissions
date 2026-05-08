class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1
        mid, row, col = -1, -1, -1

        while low <= high:
            mid = low + (high - low) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            elif matrix[row][col] > target:
                high = mid - 1
        
        return False