class Solution:
    def isPalindrome(self, x: int) -> bool:
        count = 0
        x = str(x)
        while count < len(x):
            
            if x[count] == x[-(1+count)]:
                count+=1
                pass
            else:
                return False
            
        if count == len(x):
            return True

Obj = Solution()
print(Obj.isPalindrome(121))