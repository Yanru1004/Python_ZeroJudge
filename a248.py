while True:
    try:
        a,b,n = [int(i) for i in input().strip().split(' ')]
        x = str((a*10**n)//b)

        if len(x) <= n:
            x = f'0.{"0"*(n-len(x))}' + x
        else:
            x = f'{x[:-n]}.{x[-n:]}'

        print(x)        
        
    except:
        break