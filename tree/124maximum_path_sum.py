# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float("-inf")]
        self.helper(root, ans)
        return ans[0]
    def helper(self, root, ans):
        if not root:
            return 0
        left = self.helper(root.left, ans)
        right = self.helper(root.right, ans)
        left = max(left, 0)
        right = max(right, 0)
        ans[0] = max(ans[0], root.val + left + right)
        return root.val + max(left, right)