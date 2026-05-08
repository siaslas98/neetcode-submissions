class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 2 step transformation

        # swap pos i, j with pos j, i
        # reverse each 2d list
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
    