# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def finder(root, cpath, opath ):
            if root is None:
                return 
            if cpath == "":
                cpath = str(root.val)
            else:
                cpath += "->"
                cpath += str(root.val)
            if root.left is None and root.right is None:
                opath.append(cpath)
                return 
            finder(root.left,cpath, opath)
            finder(root.right, cpath, opath)
        x = []
        finder(root, "" , x)
        return x

        
