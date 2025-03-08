
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n
        sum_numbers = total_numbers * (total_numbers + 1) // 2  # Sum of 1 to n^2
        sum_squares = total_numbers * (total_numbers + 1) * (2 * total_numbers + 1) // 6  # Sum of squares of 1 to n^2

        sum_grid = 0
        sum_squares_grid = 0

        # Calculate sum and sum of squares of the grid
        for row in grid:
            for num in row:
                sum_grid += num
                sum_squares_grid += num * num

        # Let x be the repeated number and y be the missing number
        # We have:
        # x - y = sum_grid - sum_numbers
        # x^2 - y^2 = sum_squares_grid - sum_squares
        # => (x + y)(x - y) = sum_squares_grid - sum_squares
        # => x + y = (sum_squares_grid - sum_squares) / (x - y)

        diff = sum_grid - sum_numbers  # x - y
        sum_xy = (sum_squares_grid - sum_squares) // diff  # x + y

        # Solve for x and y
        x = (diff + sum_xy) // 2
        y = (sum_xy - diff) // 2

        return [x, y]