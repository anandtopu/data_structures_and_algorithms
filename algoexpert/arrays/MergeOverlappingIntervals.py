'''
Write a function that takes in a non-empty array of arbitrary intervals,
merges any overlapping intervals, and returns the new intervals in no
particular order.
Each interval interval is an array of two integers, with
interval[0] as the start of the interval and
interval[1] as the end of the interval.
Note that back-to-back intervals aren't considered to be overlapping. For
example, [1, 5] and [6, 7] aren't overlapping;
however, [1, 6] and [6, 7] are indeed
overlapping.
Also note that the start of any particular interval will always be less than
or equal to the end of that interval.
Sample Input
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
Sample Output
[[1, 2], [3, 8], [9, 10]]
// Merge the intervals [3, 5], [4, 7], and [6, 8].
// The intervals could be ordered differently.

'''

# O(nlog(n)) time | O(n) space - where n is the length of the input array
def mergeOverlappingIntervals(intervals):
    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    # Initialize the merged intervals list with the first interval
    merged_intervals = []
    current_interval = intervals[0]
    merged_intervals.append(current_interval)

    # Iterate through the sorted intervals starting from the second interval
    for next_interval in intervals[1:]:
        current_start, current_end = current_interval
        next_start, next_end = next_interval

        # Check if the current interval overlaps with the next interval
        if current_end >= next_start:
            # Merge the intervals by updating the end of the current interval
            current_interval[1] = max(current_end, next_end)
        else:
            # No overlap, move to the next interval
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals