'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)  # Convert num to string for easy manipulation
        n = len(num_str)
        max_num = num  # Track the maximum number found

        # Try all possible swaps
        for i in range(n):
            for j in range(i + 1, n):
                num_list = list(
                    num_str
                )  # Convert the string to list for swapping

                num_list[i], num_list[j] = (
                    num_list[j],
                    num_list[i],
                )  # Swap digits at index i and j
                temp = int(
                    "".join(num_list)
                )  # Convert the list back to string and then to integer

                max_num = max(
                    max_num, temp
                )  # Update max_num if the new number is larger

        return max_num  # Return the largest number after all possible swaps