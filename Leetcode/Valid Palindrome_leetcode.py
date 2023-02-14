import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s= s.translate({ord(c): None for c in string.whitespace})
        print(s)
        s= s.translate({ord(i): None for i in "@"})
        print(s)
        s1=""
        
        for index in range(len(s)-1,-1,-1):
            s1+=s[index]
        if s1 == s :
            return True
        else:
            return False
        
        



s = "0p"
p1 = Solution()

p1.isPalindrome(s)
