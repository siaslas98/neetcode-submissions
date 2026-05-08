class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # This is a 2d problem, but if we can interpret the matrix as a flat 1d list using 2d->1d mapping we
        # can solve this in linear time

        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1

        while l <= r:
            mid = l + (r-l) // 2
            # Now convert this mid point to 2d form -> (row, col)
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

