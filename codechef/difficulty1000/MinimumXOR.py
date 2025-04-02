# cook your dish here
import sys


def solve():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        A = list(map(int, input[ptr:ptr + N]))
        ptr += N

        total_xor = 0
        for num in A:
            total_xor ^= num

        min_xor = total_xor
        for num in A:
            current_xor = total_xor ^ num
            if current_xor < min_xor:
                min_xor = current_xor

        results.append(min_xor)

    print('\n'.join(map(str, results)))


solve()