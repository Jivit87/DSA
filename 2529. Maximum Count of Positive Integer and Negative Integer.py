class Solution(object):
    def maximumCount(self, nums):
        n = len(nums)

        def neg():
            l = 0
            h = n - 1
            ans = n
            while l <= h:
                mid = (l + h) // 2

                if nums[mid] >= 0:
                    ans = mid
                    h = mid - 1
                else:
                    l = mid + 1
            return ans
        def pos():
            l = 0
            h = n - 1
            ans = n
            while l <= h:
                mid = (l + h) // 2

                if nums[mid] > 0:
                    ans = mid 
                    h = mid - 1
                    
                else:
                    l = mid + 1
            return ans 

        negative = neg()
        positive = n - pos()
        return max(negative, positive)       


