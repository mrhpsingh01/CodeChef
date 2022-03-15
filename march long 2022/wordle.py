for _ in range(int(input())):
    S = input()
    T = input()
    M = ""
    i =0 
    while i<5:
        if S[i] == T[i]:
            i += 1
            M += "G" 
        else:
            i += 1
            M += "B"
    print(M)
