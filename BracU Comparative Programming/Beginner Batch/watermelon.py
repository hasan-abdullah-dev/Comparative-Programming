weight = int(input())
check = 0

for count in range(1,weight,1):
    if count%2==0 and( weight-1)%2==0:
    
        check+=1
    
    else:
        weight-=1
    

if (check > 0):
    print("YES")

else:
    print("NO")
