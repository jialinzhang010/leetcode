# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        self.findGood(root, -float("infinity"), ans)
        return ans[0]
        
    def findGood(self, root, curMax, ans):
        if not root:
            return
        if root.val >= curMax:
            ans[0] += 1
        curMax = max(curMax, root.val)
        self.findGood(root.left, curMax, ans)
        self.findGood(root.right, curMax, ans)