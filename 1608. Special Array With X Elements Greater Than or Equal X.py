class Solution(object):
    def specialArray(self, nums):
        nums.sort()
        n = len(nums)
        for i in range(1, n+1):
            l = 0
            h = n - 1
            target = i
            ans = n
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] >= target:
                    ans = mid
                    h = mid - 1
                else:
                    l = mid + 1
            if n - ans == target:
                return target        
        return -1           
                        
