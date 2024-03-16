class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n=len(digits)
        plusOne=[0]*(n+1)

        for i in range(n-1, -1, -1):
            plusOne[i+1]=digits[i]

        if plusOne[n]!=9:
            plusOne[n]+=1
        else:
            plusOne[n]=0
            plusOne[n-1]+=1

        for i in range(n-1, -1, -1):
            if plusOne[i+1]>9:
                plusOne[i+1]=0
                plusOne[i]+=1

        if plusOne[0]==0:
            plusOne.pop(0)

        return plusOne
