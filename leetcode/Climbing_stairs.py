class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(number):
            if number == 0 or number == 1:
                return 1
            else:
                return number * factorial(number - 1)
        p = 0
        x = n//2
        for i in range(x+1):
            num_ones = n-2*i
            num_twos = i
            num_permutations = factorial(num_twos + num_ones) / (factorial(num_twos) * factorial(num_ones))
            p = p + num_permutations
        return int(p)
