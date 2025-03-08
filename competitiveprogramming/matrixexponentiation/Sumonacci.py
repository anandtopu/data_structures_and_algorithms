MOD = 10**9 + 7

def matMul(a, b):
	n1 = len(a)
	m1 = len(a[0])
	n2 = len(b)
	m2 = len(b[1])
	ret = [[0 for i in range(m2)] for j in range(n1)]
	for i in range(n1):
		for j in range(m2):
			for k in range(m1):
				ret[i][j] += (a[i][k] * b[k][j]) % MOD
				ret[i][j] %= MOD

	return ret

def matExpo(MAT, exponent):
	n = len(MAT)
	ret = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		ret[i][i] = 1
	while exponent:
		if (exponent&1):
			ret = matMul(ret, MAT)
		MAT = matMul(MAT, MAT)
		exponent >>= 1
	return ret

class Solution:

	def solve(self, A, B, C):
		SS = [0, 0, 0, 0]
		F = [0, 0, 0, 0]
		S = [0, 0, 0, 0]
		F[0] = B
		F[1] = C
		for i in range(2, 4):
			F[i] = (F[i - 2] + F[i - 1]) % MOD
		SS[0] = F[0]
		S[0] = F[0]

		for i in range(1, 4):
			S[i] = (S[i - 1] + F[i]) % MOD
			SS[i] = (SS[i - 1] + S[i]) % MOD

		base = [[0, 0, 0, 0]]
		for i in range(4):
			base[0][3 - i] = SS[i]
		MAT = [[3, 1, 0, 0], [MOD - 2, 0, 1, 0], [MOD - 1, 0, 0, 1], [1, 0, 0, 0]]

		if A <= 4:
			return SS[A - 1]
		return matMul(base, matExpo(MAT, A - 4))[0][0]