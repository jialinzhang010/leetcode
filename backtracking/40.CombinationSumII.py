class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # 涉及到去重，一定要先排序，让相同的元素并列。
        candidates.sort()
        ans = []
        path = []

        def dfs(nums, target):
            if target == 0:
                ans.append(path[:])
                return 
            if target < 0:
                return
            for i in range(len(nums)):
                # for循环形式的跳过重复项
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(nums[i + 1:], target - nums[i])
                path.pop()
                
        dfs(candidates, target)
        return ans