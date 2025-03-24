MOD = 1000000009

def multiply(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]

def matrix_expo(base, exp):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while exp > 0:
        if exp % 2 == 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exp //= 2
    return result

def count_valid_strings(N):
    if N == 0:
        return 1
    if N == 1:
        return 10

    M = [[10, -1], [1, 0]]
    result = matrix_expo(M, N - 1)

    return (result[0][0] * 10 + result[0][1] * 1) % MOD

# Read input
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(count_valid_strings(N))

