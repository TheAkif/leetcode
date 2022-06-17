class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        length = len(nums)
        
        res = []

        df = {}
        for i, value in enumerate(nums):
            sub = target - nums[i]
            
            if sub in df:
                res.append(i)
                res.append(df[sub])
                break
            else:
                df[value] = i
    
        return res
