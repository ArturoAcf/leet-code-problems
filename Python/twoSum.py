class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n=len(nums)
        indexPair=[0]*2

        for i in range(0, n):
            for j in range(1, n):
                if i!=j and nums[i]+nums[j]==target:
                    indexPair[0]=i
                    indexPair[1]=j
                    break

        return indexPair
