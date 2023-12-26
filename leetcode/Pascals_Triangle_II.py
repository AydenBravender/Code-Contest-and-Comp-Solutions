class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def factorial(number):
            if number == 0 or number == 1:
                return 1
            else:
                return number * factorial(number - 1)
        list = []
        for i in range(rowIndex+1):
            list.append(factorial(rowIndex)/(factorial(i)*factorial(rowIndex-i)))
        return list
