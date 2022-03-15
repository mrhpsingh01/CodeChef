for _ in range(int(input())):
    S =  str(input()).lower()
    arr = list(S)
    Counter = []
    c = 0                       #parameshwardas            
    P = []
    for i in range(len(arr)): # 3
            if arr[i] != arr[0] and arr[i] != arr[len(arr)-1]:
                P.append(arr[i])                              
                c += 1                                        
            elif i != 0 and i != len(arr)-1:                  
                Counter.append(c)                               
                c = 0     
    Counter.append(c)
    if max(Counter) == 0:
        print(-1)
    else:    
        print(max(Counter))
