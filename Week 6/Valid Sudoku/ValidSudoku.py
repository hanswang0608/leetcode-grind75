from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rowDicts = [{} for _ in range(n)]
        colDicts = [{} for _ in range(n)]
        gridDicts = [{} for _ in range(n)]
        
        def testThenSet(num, r, c):
            if num == '.':
                return False
            if num in rowDicts[r]:
                return True
            if num in colDicts[c]:
                return True
            g = r//3 * 3 + c//3
            if num in gridDicts[g]:
                return True
            rowDicts[r][num] = True
            colDicts[c][num] = True
            gridDicts[g][num] = True
            return False
        
        for i in range(n):
            for j in range(n):
                if testThenSet(board[i][j], i, j):
                    return False
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