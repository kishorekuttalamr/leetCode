# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        store = [0]
        def height(root):
            if root:
                lheight = height(root.left)
                rheight = height(root.right)
                store[0] = max(store[0], lheight + rheight)
                return max(lheight, rheight) + 1
            else:
                return 0
        height(root)
        return store[0]





            
        
