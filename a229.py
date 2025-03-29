def add_s(s,n):
    for i in ['(',')']:
        out = s + i
        if len(out) >= n*2:
            if out.count('(') == out.count(')'):
                print(out)

        else:
            if out.count('(') >= out.count(')'):
                add_s(out,n)

while True:
    try:
        n = int(input())
        add_s('',n)
        print('')           

    except:
        break