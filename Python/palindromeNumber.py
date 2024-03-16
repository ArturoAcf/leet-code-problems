class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False
        else:
            cad=str(x)
            n=len(cad)
            for i in range(0, n):
                if cad[i]!=cad[n-i-1]:
                    return False

        return True
