string1 = input()
string2 = input()


for index1 in range(len(string1)):
  print(string1[index1],end="")
  if index1 < len(string2):
    for index2 in range(index1,index1+1):
        print(string2[index2],end="")
        if index2 >= len(string1)-1:
            for index2 in range(index2+1,len(string2)):
                print(string2[index2],end="")


 
  