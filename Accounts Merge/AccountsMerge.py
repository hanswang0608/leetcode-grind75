from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        # build a graph of all accounts
        for account in accounts:
            for i in range(len(account)):
                if i == 0:
                    continue
                if account[i] not in graph:
                    graph[account[i]] = [account[0], set()]
                graph[account[i]][1].update(account[1:i]+account[i+1:])
        
        visited = {}
        output = []
        # use dfs to traverse all connected subgraphs
        def dfs(vertex, path):
            if vertex not in visited:
                visited[vertex] = True
                path.append(vertex)
            else:
                return
            edges = graph[vertex][1]
            for edge in edges:
                dfs(edge, path)

        # each subgraph traversed is an account, add it to output
        for account in graph:
            if account in visited:
                continue
            path = []
            dfs(account, path)
            path.sort()
            output.append([graph[path[0]][0]] + path)
        return output
            

solution = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts2 = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
solution.accountsMerge(accounts2)