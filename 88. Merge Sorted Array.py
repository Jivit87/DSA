class Solution(object):
    def merge(self, nums1, m, nums2, n):
        lArr = nums1[:m]

        ans = []
        l, r = 0, 0

        while l < len(lArr) and r < len(nums2):
            if lArr[l] < nums2[r]:
                ans.append(lArr[l])
                l += 1
            else:
                ans.append(nums2[r])
                r += 1
        while l < len(lArr):
            ans.append(lArr[l])
            l += 1
        while r < len(nums2):
            ans.append(nums2[r])
            r += 1
        
        for i in range(len(ans)):
            nums1[i] = ans[i]
