class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        memo = dict()
        def helper(i, target):
            if i == len(nums):
                if target == 0:
                    return True
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = helper(i + 1, target) or helper(i + 1, target - nums[i])
            return memo[(i, target)]
        res = helper(0, sum(nums) // 2)
        return res