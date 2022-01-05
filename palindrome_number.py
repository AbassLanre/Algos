def isPalindrome( x):    
    new_val = str(x)
    #  if new_val[-1] != new_val[0]: return False
    #  reversed_value=new_val[::-1]
    #  if reversed_value == new_val : return True
    stri =''
    for i in new_val:
        stri = i + stri
    if stri == new_val : return True
    else: return False
print(isPalindrome(123)) 