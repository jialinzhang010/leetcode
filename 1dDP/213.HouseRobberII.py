class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
        n = len(nums)
        l1 = nums[:n - 1]
        l2 = nums[1:n]

        def myrob(nums):
            if len(nums) == 1:
                return nums[0]
            dp = [0] * (len(nums))
            dp[0] = nums[0]
            dp[1] = max(nums[1], nums[0])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]
        ans1 = myrob(l1)
        ans2 = myrob(l2)
        return max(ans1, ans2)