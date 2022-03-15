for _ in range(int(input())):
    N = int(input())
    if N % 2 == 0:
        print(int(N/2))
    else:
        print(int((N+1)/2))
