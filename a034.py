while True:
    try:
        s = int(input())
        n = 0
        while s > 2 ** n:
            n += 1
            
        result = ''
        for i in range(n,-1,-1):
            if s >= 2**i:
                result += str(1)
            else:
                result += str(0)
            s %= 2**i
        if result[0] == '0':
            result = result[1:]
        print(result)
    except:
        break