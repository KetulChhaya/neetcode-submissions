# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # this can be accessible inside helper functions as well
        #other way to update the global variable is to declare it as "res=0" and inside the function, declare it as nonlocal variable
        def dfs(node): # this returns height and updates diameter not returning diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(left + right, self.res) #updates the diameter max.
            return 1 + max(left, right) #returns the height to the parent node
        dfs(root)
        return self.res
            

        