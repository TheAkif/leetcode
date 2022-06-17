class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index1 = 0
        index2 = 0
        
        res = []
        
        for i in range(n+m):
            if index1 < m and index2 >= n:
                res.append(nums1[index1])
                index1+=1
            elif index2 < n and index1 >= m:
                res.append(nums2[index2])
                index2+=1
            elif index1 < m and nums1[index1] <= nums2[index2]:
                res.append(nums1[index1])
                index1+=1
            elif index2 < n and nums2[index2] <= nums1[index1]:
                res.append(nums2[index2])
                index2+=1
                
        for i,value in enumerate(res):
            nums1[i] = value
