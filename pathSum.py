# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def summer(root,  target, summ=0):
            if root is None:
                return 0
            summ = summ+root.val
            if not root.left and not root.right:
                if summ == target:
                    return True
                return False
            left = summer(root.left , target, summ)
            if left:
                return True
            right = summer(root.right , target, summ)
            if right:
                return True
            # return 0
            
        return summer(root, targetSum)
