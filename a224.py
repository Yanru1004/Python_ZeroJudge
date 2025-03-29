while True:
    try:
        s = input()
        if s == '':
            break
        count = {}
        for a in s.lower():
            if 97 <= ord(a) <=122:
                count.setdefault(a,0)
                count[a] += 1
        if count =={}:
            print('yes !')
            continue
        odd_n = 0
        for a in count.keys():
            if count[a] %2 != 0:
                odd_n += 1
            if odd_n > 1:
                print('no...')
                break
        else:
            print('yes !')

    except:
        break