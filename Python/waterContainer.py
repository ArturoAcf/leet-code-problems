class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n=len(height)
        maxArea=-1

        i=0
        j=n-1

        while(i!=j):
            length=j-i
            area=length*min(height[i], height[j])
            maxArea=max(maxArea, area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return maxArea
