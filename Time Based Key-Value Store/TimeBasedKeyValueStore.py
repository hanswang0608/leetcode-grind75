from math import ceil

class TimeMap:

    def __init__(self):
        self.m = {}
    
    def binarySearch(self, nums, target):
        l, u = 0, len(nums)-1
        while l <= u:
            mid = ceil(l+u)
            if nums[mid][1] == target:
                return (mid, True)
            elif nums[mid][1] < target:
                l = mid+1
            else:
                u = mid-1
        return (mid, False)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.m:
        #     self.m[key] = [(value, timestamp)]
        # else:
        #     pos, found = self.binarySearch(self.m[key], timestamp)
        #     if found:
        #         self.m[key][pos] = (value, timestamp)
        #     else:
        #         self.m[key].insert(pos+1,(value, timestamp))
        if key in self.m:
            self.m[key].append((value, timestamp))
        else:
            self.m[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.m:
            return ""
        pos, found = self.binarySearch(self.m[key], timestamp)
        if found or timestamp > self.m[key][pos][1]:
            return self.m[key][pos][0]
        else:
            return ""



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
# obj.set('love','high',10)
# obj.set('love','low',20)
# print(obj.get('love',5))
# print(obj.get('love',10))
# print(obj.get('love',15))
# print(obj.get('love',20))
# print(obj.get('love',25))

obj.set('a', 'bar', 1)
obj.set('x', 'b', 3)
print(obj.get('b', 3))
obj.set('foo', 'bar2', 4)
print(obj.get('foo', 4))
print(obj.get('foo', 5))