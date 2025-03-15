class Solution(object):
    def maximumCandies(self, candies, k):
        def can_allocate(mid):
            count = 0
            for candy in candies:
                count += candy // mid
            return count >= k

        low, high = 1, max(candies)
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if can_allocate(mid):
                result = mid  
                low = mid + 1
            else:
                high = mid - 1

        return result
            
