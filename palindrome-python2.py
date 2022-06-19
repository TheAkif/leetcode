class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = ""
        temp = str(x)
        for i in range(len(str(x))):
            palindrome += str(int(x)%10)
            x = int(x)/10
            
        if palindrome == temp:
            return True
        else:
            return False
