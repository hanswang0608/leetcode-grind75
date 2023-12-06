class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    grid[i][j] = float('inf')
                else:
                    grid[i][j] = float('-inf')
        
        while queue:
            i, j = queue.popleft()
            for row, col in directions:
                r, c = i + row, j + col
                if 0 <= r < m and 0 <= c < n and grid[r][c] != -inf and grid[r][c] > grid[i][j] + 1:
                    grid[r][c] = grid[i][j] + 1
                    queue.append((r, c))
        
        highest = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == float('inf'):
                    return -1
                highest = max(grid[i][j], highest)
        
        return highest