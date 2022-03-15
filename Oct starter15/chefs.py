for _  in range(int(input())):
    N,M,K = map(int,input().split())
    A = list(map(int, input().split()))
    S = A.count(1)
    FM = A[0:M]
    CFM = FM.count(1)
    if S == N:
        print(100)
    elif CFM == M:
        print(K)
    else:
        print(0)