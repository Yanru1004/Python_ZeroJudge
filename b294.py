while True:
    try:
    
        n = input()
        price = 1
        result = 0
        for v in input().split(' '):
            result += price*int(v)
        print(result)
    except:
        break
