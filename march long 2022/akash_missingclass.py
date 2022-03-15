for _ in range(int(input())):
    N = int(input())
    if N < 6:
        print(0)
    else:
        if N % 7 != 6:
            print(int(N/7))
        else:
            print(int(N/7+1))
