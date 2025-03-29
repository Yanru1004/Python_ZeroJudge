while True:
    try:
        s = input()
        n,m = s.strip().split(' ')
        if int(n)==int(m):
            print(n)
        else:
            print(int(m)+1)
    except:
        break
