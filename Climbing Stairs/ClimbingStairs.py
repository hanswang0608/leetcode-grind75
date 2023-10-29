class Solution:
    m = {}
    def climbStairs(self, n: int) -> int:
        if n in self.m:
            return self.m[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n > 0:
            self.m[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.m[n]
        