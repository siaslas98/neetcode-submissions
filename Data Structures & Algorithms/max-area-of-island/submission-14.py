class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = set()
        res = -1
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, area, i, j):
            nonlocal res

            for direction in directions:
                dx, dy = direction
                if 0 <= i + dy < rows and 0 <= j + dx < cols and grid[i+dy][j+dx] == 1 and ((i+dy) * cols + j + dx) not in visited:
                    visited.add((i+dy) * cols + j + dx)
                    area += 1
                    res = max(res, area)
                    area = dfs(grid, area, i+dy, j+dx)

            return area

        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]
                if cell == 1 and (i * cols + j) not in visited:
                    # dfs new island
                    visited.add(i * cols + j)
                    res = max(res, 1)
                    dfs(grid, 1, i, j)
                    

        return max(res, grid[0][0], 0)