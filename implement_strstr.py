def strStr( haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    
    elif needle not in haystack:
        return -1
    
print(strStr('',''))
            
