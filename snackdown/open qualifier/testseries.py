for _  in range(int(input())):
    R = list(map(int, input().split()))
    Ri = R.count(1)
    Re = R.count(2)
    if Ri > Re:
        print("INDIA")
    elif Re > Ri:
        print("ENGLAND")
    else:
        print("DRAW")