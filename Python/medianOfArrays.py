import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedNums=np.concatenate((nums1, nums2))
        mergedNums.sort()
        n=len(mergedNums)
        oddN=int(n/2)
        evenN=int(n/2-0.5)

        if n==1:
            median=mergedNums[n-1]
        elif n%2==1:
            median=mergedNums[evenN]
        else:
            median=(mergedNums[oddN]+mergedNums[oddN-1])/2

        return median
