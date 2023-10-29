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
        
        # need to find diameter (longest path) instead of just longest path from any leaf
        def findMaxHeight(v, visited):
            if visited[v]:
                return -1
            visited[v] = True
            maxHeight = 0
            for e in mat[v]:
                maxHeight = max(1+findMaxHeight(e, visited), maxHeight)
            return maxHeight

        def getLongestPath(v, visited, path, output, depth, maxHeight):
            if visited[v]:
                return False
            visited[v] = True
            if depth == maxHeight:
                output.extend(path)
                return True
            for e in mat[v]:
                if getLongestPath(e, visited, path+[e], output, depth+1, maxHeight):
                    return True
            return False

        maxHeight = -1
        output = []
        for i in range(n):
            if len(mat[i]) == 1:
                visited = [False]*n
                maxHeight = findMaxHeight(i, visited)
                print(i, maxHeight)
                visited = [False]*n
                getLongestPath(i, visited, [i], output, 0, maxHeight)
                print(output)
                return output[floor(maxHeight/2):ceil(maxHeight/2)+1]
                
solution = Solution()
n = 7
edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
print(solution.findMinHeightTrees(n, edges))