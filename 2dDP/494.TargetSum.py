class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()

        def dfs(i, curSum):
            if i == len(nums):
                return 1 if curSum == target else 0
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            else:
                memo[(i, curSum)] = dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
                return memo[(i, curSum)]
        ans = dfs(0, 0)
        return ans
