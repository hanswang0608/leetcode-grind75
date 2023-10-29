# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[0]
    def helper(self, root):
        if root.left == None and root.right == None:
            return (0, 0)
        if root.left == None:
            r = self.helper(root.right)
            return (max(r[0], r[1]+1), r[1]+1)
        if root.right == None:
            l = self.helper(root.left)
            return (max(l[0], l[1]+1), l[1]+1)
        l = self.helper(root.left)
        r = self.helper(root.right)
        return (max(l[1] + r[1] + 2, l[0], r[0]), max(l[1], r[1])+1)