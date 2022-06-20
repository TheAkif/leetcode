class Solution:
    def climbStairs(self, n: int) -> int:
        
        mapper = [1,2,3]
        
        for i in range(2,46):
            mapper.append((mapper[i-1])+(mapper[1-2]))
                
        return mapper[n-1]
