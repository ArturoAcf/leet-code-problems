import numpy as np

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        n=len(arr)
        maxN=max(arr)
        top=arr.index(maxN)

        if n<3:
            return False

        if top==n-1 or top==0:
            return False

        for i in range(0, top):
            if arr[i]>=arr[i+1]:
                return False
        for i in range(n-1, top, -1):
            if arr[i]>=arr[i-1]:
                return False

        return True
