# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return True, 0
            left = height(root.left)
            right = height(root.right)

            bala =  left[0] and right[0] and abs(left[1]-right[1]) in [0,1]
            return bala,max(left[1],right[1])+1
        return height(root)[0]


        
