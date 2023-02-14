from math import log
class Solution:
    def isPowerOfFour(self, num: float) -> bool:
        if num <= 0:
            return False
        check1 = int(log(num) / log(4))
        check2 = log(num) / log(4)
        print(check1,check2)
        if check1 == check2:
            print(type(check2))
            return True
        else:
            return False
        

num=536870912
obj=Solution()
print(obj.isPowerOfFour(num))