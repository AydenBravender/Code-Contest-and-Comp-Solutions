class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        def list_to_int(lst):
            num = 0
            for digit in lst:
                num = num * 10 + digit
            return num
        result = list_to_int(digits) + 1
        def number_to_list(num):
            return [int(digit) for digit in str(num)]

        results = number_to_list(result)
        return results
        


           
           
           
           
           
           

        
      

