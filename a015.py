import sys

while True:
    try:
        s = sys.stdin.readline()
        n,m = s.strip().split(' ')
        old_m = []
        for i in range(int(n)):
            t = sys.stdin.readline()
            t = t.strip().split(' ')
            old_m.append(t)
        
        for i in range(int(m)):
            result = ''
            for j in range(int(n)):
                if j < int(n) - 1:
                    result += old_m[j][i] + ' '
                else:
                    result += old_m[j][i]
            print(result)

    except:
        break
