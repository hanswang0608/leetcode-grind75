# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if (root == None):
                return 0
            lheight = getHeight(root.left)
            if (lheight < 0):
                return -1
            rheight = getHeight(root.right)
            if (rheight < 0):
                return -1
            if abs(lheight - rheight) > 1:
                return -1
            return max(lheight, rheight) + 1
        return getHeight(root) != -1