import math
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))
for _  in range(int(input())):
    N, A, B = map(int,input().split())
    P = 0
    divE = []
    divO = divisors(N)
    divO.pop(0)
    for i in range(len(divO)):   
        if divO[i] % 2 == 0:
            print("ran",divO[i])
            print(divO)
            print(divE)
            divE.append(i)
            divO.pop(i)
    print(divO)
    print(divE)
    # while(N > 1):
    #     if A >= B:
    #         if N % 2 == 0:
    #             N = N / 2
    #             P = P + A
    #         else:
    #             P = P + B
    #             N = N / 3
    #     else:
    #         if N % 2 == 1:
    #             P = P + B
    #             N = N / 2
    #         else:
    #             P = P + A
    #             N = N / 2
    print(P)