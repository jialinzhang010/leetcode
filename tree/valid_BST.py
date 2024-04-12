# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, root, bottom, top):
        if not root:
            return True
        if (bottom < root.val and root.val < top):
            return self.helper(root.left, bottom, root.val) and self.helper(root.right, root.val, top)
        else:
            return False
        
