import math
'''
https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PRIME1

Prime Generator
Ram wants to generate some prime numbers for his cryptosystem. Help him please! Your task is to generate all prime numbers between two given numbers.

Warning: large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well designed)
Input Format
The first line contains t, the number of test cases (less then or equal to 10).

Followed by t lines which contain two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output Format
For every test case print all prime numbers p such that m <= p <= n, one number per line. Separate the answers for each test case by an empty line.

Constraints
(1 <= m <= n <= 1000000000, n-m<=100000)
'''

def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes


def segmented_sieve(m, n, primes):
    sieve_range = [True] * (n - m + 1)
    if m == 1:
        sieve_range[0] = False

    for p in primes:
        start = max(p * p, m + ((p - m % p) % p))
        for j in range(start, n + 1, p):
            sieve_range[j - m] = False

    primes_in_range = [i + m for i, is_prime in enumerate(sieve_range) if is_prime]
    return primes_in_range


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        m = int(data[index])
        n = int(data[index + 1])
        index += 2

        limit = int(math.sqrt(n))
        primes = sieve(limit)

        primes_in_range = segmented_sieve(m, n, primes)

        # Collect results for each test case
        results.append(primes_in_range)

    # Print results with a blank line between test cases
    for i, primes in enumerate(results):
        for prime in primes:
            print(prime)
        if i < len(results) - 1:
            print()


if __name__ == "__main__":
    main()