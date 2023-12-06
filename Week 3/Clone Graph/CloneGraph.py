"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        return self.cloneGraphHelper(node, visited)

    def cloneGraphHelper(self, node, visited):
        if not node:
            return None
        newNode = Node()
        newNode.val = node.val
        visited[node.val] = newNode
        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                self.cloneGraphHelper(neighbor, visited)
            newNode.neighbors.append(visited[neighbor.val])
        return newNode