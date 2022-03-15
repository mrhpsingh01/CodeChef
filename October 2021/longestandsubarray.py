for _  in range(int(input())):
    N = int(input())
    l = list(range(1,N+1))
    ans = [l[i:i + 2**i] for i in range(0,len(l),2**i)]
    print(ans)