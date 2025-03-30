'''
https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/POTATOES
Farmer Feb has three fields with potatoes planted in them. He harvested x potatoes from the first field, y potatoes from the second field and is yet to harvest potatoes from the third field. Feb is very superstitious and believes that if the sum of potatoes he harvests from the three fields is a prime number (http://en.wikipedia.org/wiki/Prime_number), he'll make a huge profit. Please help him by calculating for him the minimum number of potatoes that if harvested from the third field will make the sum of potatoes prime. At least one potato should be harvested from the third field.

Input
The first line of the input contains an integer T denoting the number of test cases. Each of the next T lines contain 2 integers separated by single space: x and y.



Output
For each test case, output a single line containing the answer.



Constraints
1 ≤ T ≤ 1000
1 ≤ x ≤ 1000
1 ≤ y ≤ 1000

'''
import sys

def precompute_primes(max_limit):
    sieve = [True] * (max_limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(max_limit ** 0.5) + 1):
        if sieve[num]:
            sieve[num*num : max_limit+1 : num] = [False] * len(sieve[num*num : max_limit+1 : num])
    return sieve

max_possible_sum = 2000 + 1000  # x and y can be 1000 each, z up to 1000 (but problem doesn't specify upper limit for z)
sieve = precompute_primes(max_possible_sum)

def find_min_z(x, y):
    s = x + y
    z = 1
    while True:
        if sieve[s + z]:
            return z
        z += 1

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(find_min_z(x, y))