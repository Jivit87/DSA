class Solution(object):
    def sortArray(self, nums):    
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            m = len(arr) // 2
            lArr = arr[:m]
            rArr = arr[m:]
            lSorted = mergeSort(lArr)
            rSorted = mergeSort(rArr)
            return merge(lSorted, rSorted)


        def merge(arr1, arr2):
            ans = []
            l,r = 0, 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l] < arr2[r]:
                    ans.append(arr1[l])
                    l += 1
                else:
                    ans.append(arr2[r])
                    r += 1
            while l < len(arr1):
                ans.append(arr1[l])
                l += 1
            while r < len(arr2):
                ans.append(arr2[r])
                r += 1
            return ans    


        return mergeSort(nums)

            
                
