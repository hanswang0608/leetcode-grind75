# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower = 0
        upper = n
        mid = ceil((upper - lower)/2)
        while lower < upper:
            if isBadVersion(mid):
                upper = mid
            else:
                lower = mid
            if upper-lower == 1:
                return upper
            mid = ceil((upper - lower)/2) + lower