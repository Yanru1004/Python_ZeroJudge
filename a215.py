while True:
    try:
        n,m = [int(i) for i in input().strip().split(' ')]

        s = n
        c = 0
        while s <= m:
            c += 1
            s += n+c
            
        print(c+1)
    except EOFError:
        break