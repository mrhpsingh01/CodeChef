for _ in range(int(input())):
    N, X = map(int, input().split())
    i,B,C = 0,0,0
    M = N - int(X / 3)
    S = 3 * int(X/3)
    A = int(X/3)
    while i < M:
        i += 1
        if(A + B + C != N):
            if(S < X):
                A += 1
                S += 1*3
            elif(S == X):
                
                break
            else:
                B += 1
                S -= 1       
    
    if S == X:
        C = N - (A + B)
        print("YES")
        print(A,B,C)
    else:
        print("NO")


