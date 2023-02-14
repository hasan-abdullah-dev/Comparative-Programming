s = input()

list = [0]*2
list = s[0]
print(list)

count = 0
check1 = 0
check2 =0

for var in range(count,len(s)):
    if list[0] != word:
        list[1] = s[word]
        break

for word in range(0,len(s)):
    for count in range(count,len(s)):
        if word == count:
            continue 
        elif s[word] == s[count]:
            if list[0] == s[count]:
                check1+=1    
            elif list[1] == s[count]:
                check2+=1


if (check1 >=2 and check2 >=2):
    print("Yes")
else:
    print("No")
