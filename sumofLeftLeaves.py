# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        def counter(root):
            if root is None:
                return 0
            s = 0
            if root.left and root.left.left is None and root.left.right is None:
                s += root.left.val
            
            s += counter(root.left)
            s += counter(root.right)
            return s
        
        return counter(root)
