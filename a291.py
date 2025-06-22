while True:
    try:
        pw = input()
        if pw == '':
            continue
        pw = pw.strip().split(' ')
        n = int(input())

        for i in range(n):
            guess = input().strip().split(' ')
            a = [i for i in guess]
            b = [i for i in pw]
            n = 0
            for s in range(4):
                if guess[s] == pw[s]:
                    a[s] = 'x'
                    b[s] = 'x'
            
            for s in a:
                if s =='x':
                    #print('x跳過')
                    pass
                elif s in b:
                    n += 1
                    b[b.index(s)] = 'x'

            print(f'{a.count("x")}A{n}B')
        
    except:
        break