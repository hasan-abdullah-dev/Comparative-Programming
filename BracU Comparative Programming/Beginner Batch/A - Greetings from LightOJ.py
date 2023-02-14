c=int(input())

p1=[0]*(c)
p2=[0]*(c)

for i in range(c):
     p1[i],p2[i]=input().split()
#     p2[i]=int(input())

for i in range(c):

    print("Case " + str(i+1) + ": " + str(int(p1[i])+int(p2[i])))




