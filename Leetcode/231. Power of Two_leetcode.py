from math import log
class Solution:
    def isPowerOfFour(self, n: float) -> bool:
        if n <= 0:
            return False
        check1 = int(log(n) / log(2))
        check2 = format(log(n) / log(2),"14f")
        check2=float(check2)
        print(check1,check2)
        if check1 == check2:
            return True
        else:
            return False

num=536870912
obj=Solution()
print(obj.isPowerOfFour(num))