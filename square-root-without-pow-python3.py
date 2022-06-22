class Solution:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x 
    
        for i in range(1,x+1):
            if(i*i > x):
                return i-1
        
        return -1
