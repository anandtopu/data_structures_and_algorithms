from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        lo, hi = 0, len(queries) + 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.canDo(nums, queries, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo if lo <= len(queries) else -1

    def canDo(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        length = len(nums)

        for i in range(length):
            coins = []
            for j in range(k):
                if queries[j][0] <= i <= queries[j][1]:
                    coins.append(queries[j][2])
            if not self.subsetPossible(coins, nums[i]):
                return False

        return True

    def subsetPossible(self, coins: List[int], target: int) -> bool:
        dp = [False] * (target + 1)
        dp[0] = True

        for coin in coins:
            for t in range(target, coin - 1, -1):
                dp[t] = dp[t] or dp[t - coin]

        return dp[target]