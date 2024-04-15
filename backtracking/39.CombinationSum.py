class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        def helper(candidates, target):
            if target == 0:
                ans.append(path[:])
                return
            if target < 0:
                return
            for i in range(len(candidates)):
                path.append(candidates[i])
                helper(candidates[i:], target - candidates[i])
                path.pop()
            
        helper(candidates, target)
        return ans