#leetcode | Median of Two Sorted Arrays : (https://leetcode.com/problems/median-of-two-sorted-arrays/)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            A, B, m, n = nums2, nums1, len(nums2), len(nums1)
        else:
            A, B, m, n = nums1, nums2, len(nums1), len(nums2)
            
        imin, imax = 0, m
        while 1:
            i= (imin+imax)//2
            j = (m+n+1)//2-i
            
            if (i!=0 and j!=n) and A[i-1] > B[j]:
                imax = i-1
            elif (j!=0 and i!=m) and B[j-1] > A[i]:
                imin = i+1
            else:
                break
        
        left = ([A[i-1]] if i!=0 else []) + ([B[j-1]] if j!=0 else [])
        right = ([A[i]] if i!=m else []) + ([B[j]] if j!=n else [])
        if (m+n)%2 == 1:
            return max(left)
        else:
            return (max(left)+min(right))/2