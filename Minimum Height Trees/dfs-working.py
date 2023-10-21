from typing import List
from math import floor, ceil

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return range(n)

        mat = [[] for _ in range(n)]
        for edge in edges:
            mat[edge[0]].append(edge[1])
            mat[edge[1]].append(edge[0])
        
        longestPath = []
        # find longest path in the undirected tree
        def dfs(v, last):
            nonlocal longestPath
            p1 = p2 = []
            for e in mat[v]:
                if e == last:
                    continue
                path = dfs(e, v)
                if len(path) > len(p1):
                    p2 = p1
                    p1 = path
                elif len(path) > len(p2):
                    p2 = path
            if len(p1+[v]+p2) > len(longestPath):
                longestPath = p1[::-1] + [v] + p2
            return [v] + p1
        
        dfs(0, -1)

        l = len(longestPath)
        return longestPath[ceil(l/2)-1:floor(l/2)+1]

                
solution = Solution()
n = 7
edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
print(solution.findMinHeightTrees(n, edges))