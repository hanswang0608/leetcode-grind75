mat = [
    [1,2,3,4], 
    [5,6,7,8], 
    [9,10,11,12], 
    [13,14,15,16]]

mat2 = [
    [0,1,0,0], 
    [0,0,0,0], 
    [0,0,1,0], 
    [0,0,0,0]]

mat3 = [
    [0,0,0],
    [0,1,0],
    [1,1,1]]

mat4 = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

class Solution:    
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        output = [[ -1 for k in range(len(mat[0]))] for k in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                output[i][j] = self.bfs(mat, (i,j))[1]
        return output

    def bfs(self, mat, start):
        visited = [[ False for k in range(len(mat[0]))] for k in range(len(mat))]
        queue = []
        queue.append((start, 0))
        visited[start[0]][start[1]] = True
        while queue:
            next = queue.pop(0)
            (i,j) = next[0]
            distance = next[1]
            # print(next[0], mat[i][j], distance)
            if mat[i][j] == 0:
                return next
            self.expand(next, queue, visited, mat)
    
    def expand(self, target, queue, visited, mat):
        (i,j) = target[0]
        distance = target[1]
        for k in range(4):
            new_i = i+dRow[k]
            new_j = j+dCol[k]
            if self.isValid((new_i, new_j), (len(mat),len(mat[0]))) and not visited[new_i][new_j]:
                queue.append(((new_i, new_j), distance+1))
                visited[new_i][new_j] = True

    def isValid(self, target: tuple[int, int], dimension: tuple[int, int]) -> bool:
        return target[0] >= 0 and target[0] < dimension[0] and target[1] >= 0 and target[1] < dimension[1]

solution = Solution()
output = solution.updateMatrix(mat4)
print(output)