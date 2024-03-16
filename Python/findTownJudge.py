import numpy as np

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        tam=len(trust)
        judges=np.ones((1,n), dtype=bool)
        countJ=0
        judge=-1

        if tam==0:
            if n==1:
                judge=1
            else:
                judge=-1
        else:
            for i in range(0, n):
                for j in range(0, tam):
                    if trust[j][0]==i+1:
                        judges[0][i]=False

            for i in range(0, n):
                countJ=0
                if judges[0][i]==True:
                    for j in range(0, tam):
                        if trust[j][1]==i+1:
                            countJ+=1
                            if countJ==n-1:
                                judge=i+1

        return judge
