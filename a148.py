while True:
    try:
        n = [int(i) for i in input().strip().split(' ')]

        s = sum(n[1:])/(len(n)-1)
        if s > 59:
            print('no')
        else:
            print('yes')

    except:
        break