for _ in range(int(input())):
    N, K = map(int,input().split())
    if N % 2 == 0:
        answer = (2*N-K-1) 
    else:
        answer = (2*N-K-2) 
    print(int(answer));