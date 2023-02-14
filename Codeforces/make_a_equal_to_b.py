a_count_one = 0
a_count_zero = 0
b_count_one = 0
b_count_zero = 0
change = 1
cases = int(input())
for i in range(cases):
    length = int(input())
    a = [None]*length
    b = [None]*length
    for i in range(length):
        a[i] = int(input())
        if a[i] == 1:
            a_count_one +=1
                   
        else: 
            a_count_zero +=1


    for i in range(length):
        b[i] = int(input())
        if b[i] == 1:
            b_count_one +=1
        else:
            b_count_zero +=1
    print(a_count_one, b_count_one)
    if a == b:
        print("done")

    if a_count_one == b_count_one:
        print("ola")
    else:
        change += abs(a_count_one - b_count_one)
    



    print(a)
    print(b)
    print(change)
