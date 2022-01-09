def longestCommonPrefix(strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        shortest_string=strs[0]
        prefix=''
        for i in range(len(shortest_string)):
            if strs[len(strs)-1][i]== shortest_string[i]:
                prefix+=shortest_string[i]
            else:
                break
            
    
        return prefix 
    
    