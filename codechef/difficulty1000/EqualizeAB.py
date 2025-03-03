def can_equalize(A, B, X):
    # Compute the absolute difference between A and B
    D = abs(A - B)
    # Check if the difference is divisible by 2X
    if D % (2 * X) == 0:
        return "YES"
    else:
        return "NO"

# Input reading
T = int(input())
for _ in range(T):
    A, B, X = map(int, input().split())
    print(can_equalize(A, B, X))