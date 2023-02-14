class Solution:
    def __init__(self):
        self.sum = sum
    def romanToInt(self, s: str , sum):
        
        for i in range(len(s)):
            
            if s[i] == "I":
                self.sum+=1
                check = 1
                
            elif s[i] == "V":
                self.sum+=5
                check = 5

            elif s[i] == "X":
                self.sum+=10
                check = 10
            
            elif s[i] == "L":
                self.sum+=50
                check = 50

            elif s[i] == "C":
                self.sum+=100
                check = 100

            elif s[i] == "D":
                self.sum+=500
                check = 500

            elif s[i] == "M":
                self.sum+=1000
                check = 1000

        return self.sum

            
s = input()
sum = 0
p1 = Solution()
print(p1.romanToInt(s,sum))

