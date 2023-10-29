from typing import List, Optional
from queue import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        lvl = 0
        output = []
        while queue:
            nextNode, nodeLvl = queue.popleft()
            if nodeLvl == lvl:
                lvl += 1
                output.append(nextNode.val)
            if nextNode.right:
                queue.append((nextNode.right, nodeLvl+1))
            if nextNode.left:
                queue.append((nextNode.left, nodeLvl+1))
        return output
            
        

solution = Solution()
l = TreeNode(2, None, TreeNode(5))
r = TreeNode(3, None, None)
root = TreeNode(1, l, r)
print(solution.rightSideView(root))