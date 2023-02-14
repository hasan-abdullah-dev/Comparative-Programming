string = input()
count = 0
upper_bool = False
lower_bool = False
digit_bool = False
error_bool = False

for check in string:
    count+=1 

    if check.isupper():
        upper_bool = True
        
    elif check.islower():
        lower_bool = True

    elif check.isdigit():
        digit_bool = True
        
    elif check in ["!", "?", ".", ",", "_"]:
        pass
    
    else:
        error_bool = True 

if error_bool ==  True:
    print("Too weak")
    
elif count >= 5 and upper_bool == True and lower_bool == True and digit_bool == True:
    print("Correct")

else:
    print("Too weak")
