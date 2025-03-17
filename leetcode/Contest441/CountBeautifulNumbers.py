class Solution:
    def __init__(self):
        self.hm = {}

    def beautifulNumbers(self, l: int, r: int) -> int:
        return int(self.f(r) - self.f(l - 1))

    def f(self, n: int) -> int:
        if n < 0:
            return 0
        self.hm = {}
        return self.g(str(n), 0, True, False, 0, 1)

    def g(self, s: str, i: int, t: bool, st: bool, su: int, pr: int) -> int:
        if i == len(s):
            if not st:
                return 0
            return 1 if su != 0 and pr % su == 0 else 0

        key = f"{i}_{1 if t else 0}_{1 if st else 0}_{su}_{pr}"
        if key in self.hm:
            return self.hm[key]

        res = 0
        lim = int(s[i]) if t else 9
        for d in range(lim + 1):
            nt = t and (d == lim)
            if not st and d == 0:
                res += self.g(s, i + 1, nt, False, su, pr)
            else:
                res += self.g(s, i + 1, nt, True, su + d, pr * d if st else d)

        self.hm[key] = res
        return res