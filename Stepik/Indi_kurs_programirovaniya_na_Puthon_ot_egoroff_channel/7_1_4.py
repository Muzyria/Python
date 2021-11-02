def check_password(s):
    digit = 0
    up = 0
    simbol = 0
    lens = 0
    flag = False
    if len(s) >= 10:
        for i in s:
            if i.isupper():
                up += 1
            if up > 0:
                for i in s:
                    if i.isdigit():
                        digit += 1
                    if digit >= 3:
                        for i in s:
                            if i in "!@#$%*":
                                simbol += 1
                            if simbol > 0:
                                flag = True 
                                
    if flag:                            
        print('Perfect password')
    else:
        print('Easy peasy')