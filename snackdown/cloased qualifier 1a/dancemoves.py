for _ in range(int(input())):
    X, Y = map(int,input().split())
    D = Y - X
    mov = 0
    for i in range(abs(X)+abs(Y)):
        if D > 0:
            if D == 1:
                D = D + 1
                mov += 1 
            else:
                D = D - 2
                mov += 1 
        elif D < 0:
            if D == -1:
                D = D - 1
                mov += 1
            else:
                D = D + 2
                mov += 1
        else:
            print(mov)
            break
    