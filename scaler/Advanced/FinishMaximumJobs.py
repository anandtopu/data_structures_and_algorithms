'''
Finish Maximum Jobs

Problem Description
There are N jobs to be done, but you can do only one job at a time.
Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.
Your aim is to select jobs in such a way so that you can finish the maximum number of jobs.
Return the maximum number of jobs you can finish.

Problem Constraints
1 <= N <= 105
1 <= A[i] < B[i] <= 109

Input Format
The first argument is an integer array A of size N, denoting the start time of the jobs.
The second argument is an integer array B of size N, denoting the finish time of the jobs.

Output Format
Return an integer denoting the maximum number of jobs you can finish.'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)

        # store the start and finish time of a job
        v = []

        for i in range(n):
            v.append([A[i], B[i]])

        # Sort the jobs in ascending order of finish time
        v.sort(key=lambda x: x[1])

        # Since we can do at least one job, initialize the answer to 1
        ans = 1

        # Finish time of the first job
        lst = v[0][1]

        for i in range(1, n):
            # If the start time of the next job is greater than or equal to the finish time of the last job we are working on
            # then update finish time and increment ans
            if v[i][0] >= lst:
                ans += 1
                lst = v[i][1]

        return ans