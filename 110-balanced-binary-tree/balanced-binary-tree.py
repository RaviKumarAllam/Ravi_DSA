# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal= [True]
 
        def height(root):
            if not root:
                return 0
 
            l_hei= height(root.left)
            if bal[0] is False:
                return 0
 
 
            r_hei = height(root.right)
            if abs(l_hei - r_hei) > 1:
                bal[0] = False
                return 0
            return 1 + max(l_hei, r_hei)
 
        height(root)
        return bal[0]
  