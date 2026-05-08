class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 4 direction you can traverse
        # cycle through these direction in the following order: right, down, left, and up
        # 2 conditions for switching directions: border or already visited cell
        # once a direction switch is not possible any more, exit loop

        rows = len(matrix) # rows
        cols = len(matrix[0]) # cols

        i, j = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        dir_idx = 0
        visited = set()
        res = []

        while True:
            res.append(matrix[j][i])
            visited.add((j, i))

            if (len(res) == rows * cols):
                return res 

            next_i, next_j = i + directions[dir_idx][1], j + directions[dir_idx][0]

            if next_i == cols or next_i < 0 or next_j == rows or next_j < 0 or (next_j, next_i) in visited:
                dir_idx = (dir_idx + 1) % 4
                
            i += directions[dir_idx][1]
            j += directions[dir_idx][0]
            




