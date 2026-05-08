class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in s:
                    return False
                s.add(board[i][j])
            s.clear()
        
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in s:
                    return False
                s.add(board[j][i])
            s.clear()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != '.' and board[i+k][j+l] in s:
                            return False
                        s.add(board[i+k][j+l])
                s.clear()
            
        
        return True
            




