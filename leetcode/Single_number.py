class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for number in nums:
            if number not in num_dict:
                num_dict[number] = None
            else:
                del num_dict[number]
        first_key, first_value = next(iter(num_dict.items()))
        return first_key


        
