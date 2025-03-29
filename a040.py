while True:
    try:
        n,m = [int(i) for i in input().strip().split(' ')]
        
        result=[]
        for i in range(n,m+1):
            k = 0
            for j in str(i):
                k += int(j)**len(str(i))
            if k == i:
                result += [str(i)]
                
        if len(result) != 0:
            print(' '.join(result))
        else:
            print('none')

    except:
        break