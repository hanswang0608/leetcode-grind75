from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        rootInd = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:rootInd+1], inorder[:rootInd])
        root.right = self.buildTree(preorder[rootInd+1:], inorder[rootInd+1:])
        return root

solution = Solution()
# preorder, inorder = [3,9,11,13,20,15,7], [11,9,13,3,15,20,7]
preorder, inorder = [3,9,20,15,7], [9,3,15,20,7]
solution.buildTree(preorder, inorder)