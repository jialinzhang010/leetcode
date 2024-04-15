class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def helper(nums):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    helper(nums)
                    path.pop()
        helper(nums)
        return ans