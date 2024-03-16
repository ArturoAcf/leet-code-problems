class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        numberBin=bin(n)
        onesCount=numberBin.count("1")

        return onesCount
