def are_all_same(lst):
            return all(x == lst[0] for x in lst)
        
        prefix = []    
        x = True
        i = 0
        while x:
            list = []
            for word in strs:
                if i < len(word):
                    list.append(word[i])
                else:
                    x = False
                    break
            if x and are_all_same(list):
                prefix.append(list[0])
                i += 1
            else:
                break
        return ''.join(prefix)
