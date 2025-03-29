AN = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21,\
     'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}

s_group = {}
for i in AN.keys():
    n = AN[i]//10 + (AN[i]%10 * 9)
    s_group.setdefault(n%10,'')
    s_group[n%10] += i

while True:
    try:
        s = input()
        n = 0
        for i in range(0,8):
            n += int(s[i])*(8-i)
        n = (10-(n + int(s[8]))%10)%10
        print(s_group[n])
    except:
        break
    