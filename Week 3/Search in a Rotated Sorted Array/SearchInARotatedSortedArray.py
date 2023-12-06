class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        if nums[-1] < nums[0]:
            l, u = 0, len(nums)-1
            mid = 0
            while l < u:
                mid = ceil((u-l)/2) + l
                if nums[mid] < nums[-1]:
                    u = mid
                elif nums[mid] > nums[-1]:
                    l = mid
                if u - l == 1:
                    break
            nums = nums[mid:] + nums[:mid]
            pivot = mid

        if nums[0] == target:
            return pivot
        elif nums[-1] == target:
            return (len(nums)-1 + pivot) % len(nums)

        l, u = 0, len(nums)-1
        mid = -1
        while l < u:
            mid = ceil((u-l)/2) + l
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                u = mid
            elif nums[mid] == target:
                return (mid + pivot) % len(nums)
            if u - l == 1:
                return-1
        return -1
        
