for _ in range(1):
    N =  str(1011) #int(input())
    arr,arr2 = list(N),list(N)
    i = 0
    for i in range(len(arr)):
        if(i < len(arr)-1):
            arr2.append(arr[i]+arr[i+1])
        else:
            arr2.append(arr[len(arr)-i-1] + arr[len(arr)-i] + arr[len(arr)-i+1])
    print(arr2)
    print(arr)