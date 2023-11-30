# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return inorder(root)[k-1]
        
solution = Solution()
l = TreeNode(1, None, TreeNode(2))
r = TreeNode(4)
root = TreeNode(3, l, r)
print(solution.kthSmallest(root, 1))