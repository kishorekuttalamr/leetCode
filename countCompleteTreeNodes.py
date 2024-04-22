# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def counter(root):
            if root is None:
                return 0
            left = counter(root.left)
            right = counter(root.right)
            return left+right+1
        return counter(root)
        
