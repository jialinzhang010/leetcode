class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 画出二叉树，具体分析每个节点的子节点能否买/卖/冷
        dp = {}  # key = {i, buying}  val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)  # 第一个节点必须买

