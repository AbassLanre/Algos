def pangram(s):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    new_s = s.lower()
    
    for i in alphabets:
        if i not in new_s:
            return False

    return True
    
print(pangram('bcdefghijklmnopqrstuvwxyz'))