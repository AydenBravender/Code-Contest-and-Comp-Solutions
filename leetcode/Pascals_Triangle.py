class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

        def binomial_coefficient(n, k):
            return factorial(n) / (factorial(k) * factorial(n - k))

        def expand_expression(numRows):
            output = []
            for i in range(numRows):
                row = []
                for j in range(i + 1):
                    # Calculate the binomial coefficient
                    coef = binomial_coefficient(i, j)
                    # Substitute x=1 and y=1 into x^(n-k)*y^k
                    term_with_values = coef * (1 ** (i - j)) * (1 ** j)
                    row.append(int(term_with_values))
                output.append(row)
            return output
        return(expand_expression(numRows))

            


                
            
            


        
        
