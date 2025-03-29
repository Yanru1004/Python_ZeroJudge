while True:
    try:
        n = int(input())
        if n == 0: break
        result =[]
        for i in range(1,n):
            if i %7 ==0:
                continue
            result.append(str(i))
            
        print(' '.join(result))

    except:
        break