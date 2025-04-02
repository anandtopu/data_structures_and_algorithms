import math

def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(T):
        N = int(input[ptr])
        A = int(input[ptr + 1])
        ptr += 2
        k = int(math.isqrt(N))
        results.append(k * A)
    print('\n'.join(map(str, results)))

solve()