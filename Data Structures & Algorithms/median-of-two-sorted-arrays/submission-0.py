class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, m, n, ans= 0, 0, len(nums1), len(nums2), []
        while(i<m and j<n):
            if(nums1[i]<=nums2[j]):
                ans.append(nums1[i])
                i+=1
            elif nums2[j]<nums1[i]:
                ans.append(nums2[j])
                j+=1
        while(i<m):
            ans.append(nums1[i])
            i+=1
        while(j<n):
            ans.append(nums2[j])
            j+=1
        if len(ans)%2 == 0:
            return (ans[len(ans)//2]+ ans[(len(ans)//2)-1])/2
        else:
            return ans[len(ans)//2]
