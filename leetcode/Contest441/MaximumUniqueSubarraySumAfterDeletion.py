from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        sum = 0
        has_non_negative = False

        # Include one copy of each non-negative number
        for num in nums:
            if num >= 0:
                has_non_negative = True
                if num not in seen:
                    seen.add(num)
                    sum += num

        # If there is at least one non-negative, return the sum of distinct non-negatives.
        if has_non_negative:
            return sum
        else:
            # All elements are negative: return the maximum (least negative) element.
            max_negative = nums[0]
            for num in nums:
                if num > max_negative:
                    max_negative = num
            return max_negative