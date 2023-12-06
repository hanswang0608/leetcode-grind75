class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        print(graph)
        visited = [False] * numCourses
        recurStack = [False] * numCourses
        for course in range(numCourses):
            if self.dfs(course, graph, visited, recurStack):
                return False
        return True
    
    # Use depth first search to look for a cycle in the graph.
    # A cycle means cyclic dependency so the courses cannot be finished.
    # Lack of cycles == canFinish
    def dfs(self, source, graph, visited, recurStack):
        if visited[source]:
            return False
        else:
            visited[source] = True
        recurStack[source] = True
        for dependency in graph[source]:
            if recurStack[dependency]:
                return True
            elif not visited[dependency]:
                if self.dfs(dependency, graph, visited, recurStack):
                    return True
        recurStack[source] = False
        return False