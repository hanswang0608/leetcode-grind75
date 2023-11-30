from collections import Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        boardCount = {}
        wordCount = Counter(word)
        for r in range(m):
            for c in range(n):
                if board[r][c] not in boardCount:
                    boardCount[board[r][c]] = 0
                boardCount[board[r][c]] += 1
        for c in wordCount:
            if c not in boardCount or boardCount[c] < wordCount[c]:
                return False
        

        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        def checkAdjacent(r, c, word, visited):
            if word[0] != board[r][c] or visited[r][c]:
                return False
            word = word[1:]
            if not word:
                return True
            visited[r][c] = True
            for dr, dc in dirs:
                if 0 <= r+dr < m and 0 <= c+dc < n and checkAdjacent(r+dr, c+dc, word, visited):
                    return True
            visited[r][c] = False
            return False
        for r in range(m):
            for c in range(n):
                visited = [[False]*n for _ in range(m)]
                if checkAdjacent(r, c, word, visited):
                    return True
        return False
        

solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
word2 = "SEE"
word3 = "ABCB"
word4 = "XYZ"
print(solution.exist(board, word4))