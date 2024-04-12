# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.findLength(root, ans)
        return ans[0]
    def findLength(self, root, ans):
        if not root: return -1
        left, right = self.findLength(root.left, ans), self.findLength(root.right, ans)
        ans[0] = max(ans[0], 2 + left + right)
        return max(left, right) + 1

        