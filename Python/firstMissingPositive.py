import numpy as np

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minN=1
        limit=np.abs(max(nums)+1)

        num_set=set(nums)

        for i in xrange(1, limit+1):
            if i not in num_set:
                minN=i
                break

        return minN
