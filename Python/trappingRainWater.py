import numpy as np

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height=height
        water=np.zeros_like(height)
        n=len(height)
        lMax=np.zeros(n)
        rMax=np.zeros(n)
        lMax[0]=height[0]
        rMax[n-1]=height[n-1]

        for i in range(1,n):
            lMax[i]=max(lMax[i-1], height[i])
        for i in range(n-2, -1, -1):
            rMax[i]=max(rMax[i+1], height[i])
        for i in range(n):
            border=min(lMax[i], rMax[i])
            if(border>height[i]):
                water[i]=border-height[i]

        return int(sum(water))
