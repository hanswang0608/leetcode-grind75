from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        n, m, curDir = 0, 0, 0
        output = []
        for _ in range(rows*cols):
            visited[n][m] = True
            output.append(matrix[n][m])
            n, m = n + directions[curDir][0], m + directions[curDir][1]
            if not (0 <= n < rows and 0 <= m < cols) or visited[n][m]:
                n, m = n - directions[curDir][0], m - directions[curDir][1]
                curDir += 1
                if curDir == len(directions):
                    curDir = 0
                n, m = n + directions[curDir][0], m + directions[curDir][1]
        return output
            
solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix))