class Solution(object):
    def reverse(self, x):
        negative=False
        if(x < 0):
            negative=True
            x*=-1

        if(x % 10 == 0):
            x/=10

        st=str(x)
        revers=st[::-1]
        ans=int(revers)

        if(negative):
            ans*=-1
        if(ans > 2**31-1 or ans < -2**31):
            return 0

        return ans
