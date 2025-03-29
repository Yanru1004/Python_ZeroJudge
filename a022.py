while True:
    try:
        s = input()
        q = ''
        for i in range(len(s)):
            q += s[len(s)-i-1]

        if s == q:
            print('yes')
        else:
            print('no')
    except:
        break
