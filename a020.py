
AN = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21,\
     'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}

while True:
    try:
        s = input()
        n = AN[s[0]]
        c1 = (n%10)*9+(n//10)
        c2 = 0
        for i in range(1,9):
            c2 += int(s[i]) * (9-i)
        c3 = c1 + c2 + int(s[9])
        
        if c3%10 == 0:
            print('real')
        else:
            print('fake')
    except:
        break 
