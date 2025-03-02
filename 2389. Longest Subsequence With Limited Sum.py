class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)  
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        def binary(target):
            left = 0
            right = len(prefix) - 1 
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right  
        result = []
        for i in queries:
            result.append(binary(i))  
        return result     

        
