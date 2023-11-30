from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(len(board))]
        colSets = [set() for _ in range(len(board))]
        gridSets = [set() for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board)):

                if board[i][j] == '.':
                    continue
                
                g = i//3 * 3 + j//3

                if board[i][j] in rowSets[i]: return False
                else: rowSets[i].add(board[i][j])

                if board[i][j] in colSets[j]: return False
                else: colSets[j].add(board[i][j])

                if board[i][j] in gridSets[g]: return False
                else: gridSets[g].add(board[i][j])

        return True


solution = Solution()
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))