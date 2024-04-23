class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            curMax, curMin = max(curMax * n, curMin * n, n), min(curMax * n, curMin * n, n)
            ans = max(ans, curMax)
        return ans