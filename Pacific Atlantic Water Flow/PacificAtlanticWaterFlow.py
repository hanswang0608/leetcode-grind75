from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # define cells of the pacific coast
        pacificCoast = [(0, c) for c in range(n)]
        pacificCoast.extend([(r, 0) for r in range(1, m)])
        canFlowToPacific = [[False for _ in range(n)] for _ in range(m)]

        # dfs to traverse from lower to higher cells from pacific coast
        # each cell that is visited can flow to pacific ocean because it is higher
        def dfsFromPacific(r, c, canFlowToPacific):
            if canFlowToPacific[r][c]: 
                return
            canFlowToPacific[r][c] = True
            for dr, dc in dirs:
                i, j =  r+dr, c+dc
                if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[r][c]:
                    dfsFromPacific(i, j, canFlowToPacific)
        
        # run dfs from every cell on the pacific coast
        for r, c in pacificCoast:
            if canFlowToPacific[r][c]: 
                continue
            dfsFromPacific(r, c, canFlowToPacific)

        # define cells of the atlantic coast
        atlanticCoast = [(m-1, c) for c in range(n)]
        atlanticCoast.extend([(r, n-1) for r in range(0, m-1)])
        canFlowToAtlantic = [[False for _ in range(n)] for _ in range(m)]
        output = []

        # dfs to traverse from lower to higher cells from atlantic ocean
        # each cell that is visited can flow to atlantic ocean because it is higher
        # if cell can also flow to pacific ocean, add it to output
        def dfsFromAtlantic(r, c, canFlowToAtlantic):
            if canFlowToAtlantic[r][c]: 
                return
            canFlowToAtlantic[r][c] = True
            if canFlowToPacific[r][c]:
                output.append([r, c])
            for dr, dc in dirs:
                i, j =  r+dr, c+dc
                if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[r][c]:
                    dfsFromAtlantic(i, j, canFlowToAtlantic)

        # run dfs from every cell on the atlantic coast
        for r, c in atlanticCoast:
            if canFlowToAtlantic[r][c]: 
                continue
            dfsFromAtlantic(r, c, canFlowToAtlantic)

        return output

solution = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(solution.pacificAtlantic(heights))