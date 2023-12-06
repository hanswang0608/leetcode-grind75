# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return (True, float('inf'), float('-inf'))
            l = helper(root.left)
            r = helper(root.right)
            return (l[2] < root.val < r[1] and l[0] and r[0], min(root.val, l[1]), max(root.val, r[2]))
        return helper(root)[0]