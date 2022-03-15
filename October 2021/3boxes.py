for _  in range(int(input())):
    A, B, C, D = map(int,input().split())
    add = A + B + C
    if add != 0 and D != 0:
        num = (A + B + C)/D   
        if num < 3 :
            if num <= 1:
                print("1")
            if num > 1 and num < 2:
                print("2")
            if num > 2 and num < 3:
                print("3")
        else:
            pass