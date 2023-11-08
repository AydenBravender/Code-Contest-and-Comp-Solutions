value = 0
        prev = 'E'
        for char in s:
            
            if char == 'I':
                value = value + 1
                prev = 'I'
            
            if char == 'V':
                if prev == 'I':
                    value = value + 3
                else:
                    value = value + 5
                prev = 'V'
            
            if char == 'X':
                if prev == 'I':
                    value = value + 8
                else:
                    value = value + 10
                prev = 'X'
            
            if char == 'L':
                if prev == 'X':
                    value = value + 30
                else:
                    value = value + 50
                prev = 'L'
            
            if char == 'C':
                if prev == 'X':
                    value = value + 80
                else:
                    value = value + 100
                prev = 'C'
            
            if char == 'D':
                if prev == 'C':
                    value = value + 300
                else:
                    value = value + 500
                prev = 'D'
                
            
            if char =='M':
                if prev == 'C':
                    value = value + 800
                else:
                    value = value + 1000
                prev = 'M'
                

        return value
