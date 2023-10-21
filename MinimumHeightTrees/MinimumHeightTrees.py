from typing import List
from math import floor, ceil

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return range(n)

        mat = [set() for _ in range(n)]
        for edge in edges:
            mat[edge[0]].add(edge[1])
            mat[edge[1]].add(edge[0])
        
        leaves = [i for i in range(n) if len(mat[i])==1]
        count = 0
        while (n-count) > 2:
            newLeaves = []
            for leaf in leaves:
                connection = mat[leaf].pop()
                mat[connection].remove(leaf)
                if len(mat[connection]) == 1:
                    newLeaves.append(connection)
                count += 1
            leaves = newLeaves

        return leaves


                
solution = Solution()
n = 6
edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
edges2 = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(solution.findMinHeightTrees(n, edges2))