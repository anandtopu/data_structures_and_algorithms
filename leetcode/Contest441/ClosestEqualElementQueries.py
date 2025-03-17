from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        result = []

        # Map each value to its indices in the array
        index_map = defaultdict(list)
        for i in range(n):
            index_map[nums[i]].append(i)

        # Process each query from queries
        for qi in queries:
            v = nums[qi]
            indices = index_map[v]
            if len(indices) == 1:
                result.append(-1)
            else:
                p = bisect.bisect_left(indices, qi)
                p1 = indices[(p - 1 + len(indices)) % len(indices)]
                p2 = indices[(p + 1) % len(indices)]
                d1 = self.d(qi, p1, n)
                d2 = self.d(qi, p2, n)
                result.append(min(d1, d2))

        return result

    @staticmethod
    def d(i: int, j: int, n: int) -> int:
        diff = abs(i - j)
        return min(diff, n - diff)