from enum import Enum

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        class Direction(Enum):
            UP = (0, -1)
            DOWN = (0, 1)
            LEFT = (-1, 0)
            RIGHT = (1, 0)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    print(s)
                    return False
                s.add(board[i][j])
            s.clear()

        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    print(s)
                    return False
                s.add(board[j][i])
            s.clear()


        movements = [Direction.RIGHT, Direction.RIGHT, Direction.DOWN, 
                    Direction.LEFT, Direction.LEFT, Direction.DOWN, 
                    Direction.RIGHT, Direction.RIGHT]
        

        for i in range(9):
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    if board[i][j] != '.':
                        s.add(board[i][j])
                    cur_i, cur_j = i, j
                    for move in movements:
                        dx, dy = move.value
                        new_i = cur_i + dx
                        new_j = cur_j + dy

                        if board[new_i][new_j] in s:
                            print(s)
                            return False
                        
                        if board[new_i][new_j] != '.':
                            s.add(board[new_i][new_j])

                        cur_i, cur_j = new_i, new_j

                    s.clear()
        
        return True





        