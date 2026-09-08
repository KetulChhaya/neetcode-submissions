# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.print_levels(root)
        if not root: return None

        root.left, root.right = root.right, root.left

        print(root, root.left, root.right)

        self.invertTree(root.left)
        self.invertTree(root.right)
        
    
        return root
    
    def print_levels(self, root):
        if not root: return

        curr = [root]
        while curr:
            print(" ".join(str(node.val) for node in curr))

            nxt = []
            for node in curr:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            curr = nxt



