# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left = max(left, 0)
            right = max(right, 0)

            res[0] = max(res[0], left+right+node.val) #update as a global variable but this is not we're returning as a value of dfs function
            return node.val + max(left, right) #returns the height (+1: path to the parent from its children) + max(children's height)
        dfs(root)
        return res[0]