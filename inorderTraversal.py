# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li = []
        def travserse(root):
            if root:
                travserse(root.left)
                li.append(root.val)
                travserse(root.right)
        travserse(root)
        return li
