for _ in range(int(input())):
    A, B = map(int,input().split())
    if A == 0 and B == 0:
        pass
    else:
        if A == 0 :
            print("Liquid")
        if B == 0:
            print("Solid")
        if A > 0 and B > 0:
            print("Solution")

