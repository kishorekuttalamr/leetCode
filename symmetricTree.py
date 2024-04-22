# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checker(leftr, rightr):
            if not leftr and not rightr:
                return True
            if not leftr or not rightr:
                return False
            return (leftr.val == rightr.val) and checker(leftr.left, rightr.right) and checker(leftr.right, rightr.left)


        if not root:
            return True
        return checker(root.left, root.right)
