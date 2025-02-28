class Solution(object):
    def kWeakestRows(self, mat, k):
        m = len(mat)
        nums = []
        for i in range(m):
            arr = mat[i]
            n = len(arr)
            l = 0
            h = n - 1
            ans = n
            while l <= h:
                mid = (l + h) // 2
                if arr[mid] == 0:
                    ans = mid
                    h = mid - 1
                else:
                    l = mid + 1
            nums.append((ans, i)) 
        nums.sort()
        li = [nums[i][1] for i in range(k)]     
        return li  

               
        
