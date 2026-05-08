class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through the 2d list
        # If the value at the index is a 1, perform dfs and mark visited positions
        # increment island

        numRows = len(grid)
        numCols = len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col, visited):

            visited.add((row, col))
            # left dfs
            if col - 1 >= 0 and (row, col-1) not in visited and grid[row][col-1] == "1":
                dfs(row, col-1, visited)
            if col + 1 < numCols and (row, col+1) not in visited and grid[row][col+1] == "1":
                dfs(row, col+1, visited)
            if row - 1 >= 0 and (row-1, col) not in visited and grid[row-1][col] == "1":
                dfs(row-1, col, visited)
            if row + 1 < numRows and (row+1, col) not in visited and grid[row+1][col] == "1":
                dfs(row+1, col, visited)
            
        for i in range(numRows):
            for j in range(numCols):
                if (i, j) in visited:
                    continue
                if grid[i][j] == "1":
                    dfs(i, j, visited)
                    res += 1 
        
        return res
