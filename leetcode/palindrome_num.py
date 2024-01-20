class Solution(object):
    def isPalindrome(self, x):
        x1 = str(x)
        try:
            return x1[0] == x1[-1] and x1[1] == x1[-2] and x1[2] == x1[-3] and x1[4] == x1[-5]
        except IndexError:
            return x1[0] == x1[-1]
        
       
