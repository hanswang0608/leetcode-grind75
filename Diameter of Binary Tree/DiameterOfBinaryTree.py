# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        # returns depth of root
        def dfs(root):
            nonlocal diameter
            if not root:
                return -1
            l = dfs(root.left)
            r = dfs(root.right)
            diameter = max(diameter, l+r+2)
            return 1+max(l, r)
        dfs(root)
        return diameter
    
solution = Solution()
l = TreeNode(2, TreeNode(4), TreeNode(5))
r = TreeNode(3)
root = TreeNode(1, l, r)
print(solution.diameterOfBinaryTree(root))