
def ispalindrome(s):
    startindex = 0
    endindex=len(s) - 1
    
    for x in s:
        if s[startindex] != s[endindex]:
            return False
    return True
    
print(ispalindrome("racecar"))  
 