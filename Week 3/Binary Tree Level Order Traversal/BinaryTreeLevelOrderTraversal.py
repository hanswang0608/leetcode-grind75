# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        output = []
        while queue:
            next = queue.pop(0)
            nextNode = next[0]
            depth = next[1]
            res = self.expand(nextNode, queue, depth)
            if res != None:
                if len(output) < depth+1:
                    output.append([res])
                else:
                    output[depth].append(res)
        return output

    def expand(self, root, queue, depth):
        if not root:
            return None
        if root.left:
            queue.append((root.left, depth+1))
        if root.right:
            queue.append((root.right, depth+1))
        return root.val