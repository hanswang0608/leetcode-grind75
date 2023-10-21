from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        mat = [[] for _ in range(n)]
        for edge in edges:
            mat[edge[0]].append(edge[1])
            mat[edge[1]].append(edge[0])

        def dfs(v, visited, minSoFar, curHeight):
            if curHeight > minSoFar:
                return float('inf')
            if visited[v]:
                return 0
            visited[v] = True
            maxHeight = 0
            for e in mat[v]:
                maxHeight = max(1+dfs(e, visited, minSoFar, curHeight+1), maxHeight)
                if maxHeight == float('inf'):
                    return float('inf')
            return maxHeight
        
        heights = [0]*n
        minHeight = float('inf')
        for i in range(n):
            visited = [False]*n
            heights[i] = dfs(i, visited, minHeight, 0)
            minHeight = min(minHeight, heights[i])

        output = []
        for i in range(n):
            if heights[i] == minHeight:
                output.append(i)
        return output
            

solution = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(solution.findMinHeightTrees(n, edges))