class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # 涉及到去重，一定要先排序，让相同的元素并列。
        nums = sorted(nums)
        path = []
        ans = []
        def dfs(i):
            if i == len(nums):
                ans.append(path[:])
                return
            path.append(nums[i])
            dfs(i + 1)

            path.pop()
            # 二叉树形式的递归，跳过重复项
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
            

        dfs(0)
        return ans