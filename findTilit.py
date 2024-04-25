# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        store = [0]
        def tilter(root):
            if root is None:
                return 0
            left = tilter(root.left)
            right = tilter(root.right)
            store[0] += abs(left-right)
            # return abs(left - right)
            return left + right + root.val
        tilter(root)
        return store[0]
        
