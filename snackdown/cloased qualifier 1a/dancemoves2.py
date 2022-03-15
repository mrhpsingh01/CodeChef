for _ in range(int(input())):
    X, Y = map(int,input().split())
    D = Y - X
    mov = 0
    for i in range(1000): 
        if D > 0: 
            if D % 2 == 0:    
                mov = mov + D//2
                break
            else:        
                D = D + 1
                mov += 1
        elif D < 0:      
            if D % 2 == 0:         
                mov = mov + D//2
                break
            else:          
                D = D - 1
                mov += 1
        else:
            break
    print(mov)
