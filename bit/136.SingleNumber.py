class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 两个相同数字的xor等于0
        # 0 xor 任何数字 = 原数
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans