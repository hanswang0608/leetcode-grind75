class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirRow = [-1, 0, 1, 0]
        dirCol = [0, 1, 0, -1]
        visited = []
        islands = 0
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[i])):
                col.append(False)
            visited.append(col)

        def validPos(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i])

        def dfs(i, j):
            if grid[i][j] == '0':
                return
            for k in range(4):
                if validPos(i+dirRow[k], j+dirCol[k]) and not visited[i+dirRow[k]][j+dirCol[k]]:
                    visited[i+dirRow[k]][j+dirCol[k]] = True
                    dfs(i+dirRow[k], j+dirCol[k])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    islands += 1
                    dfs(i, j)
        return islands
            