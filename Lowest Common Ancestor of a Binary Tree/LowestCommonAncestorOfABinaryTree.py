# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target1, target2, ans):
            if not root:
                return False
            if root.val == target1 or root.val == target2:
                l = dfs(root.left, target1, target2, ans)
                r = dfs(root.right, target1, target2, ans)
                if l or r:
                    ans.append(root)
                return True
            l = dfs(root.left, target1, target2, ans)
            r = dfs(root.right, target1, target2, ans)
            if l and r:
                ans.append(root)
            return l or r
        ans = []
        dfs(root, p.val, q.val, ans)
        return ans[0]