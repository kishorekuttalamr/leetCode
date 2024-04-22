# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not node1 and not node2:
                yield True
            elif not node1 or not node2:
                yield False
            elif node1.val != node2.val:
                yield False
            else:
                yield from traverse(node1.left, node2.left)
                yield from traverse(node1.right, node2.right)

        return all(traverse(p, q))

        

