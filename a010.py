import sys

s = sys.stdin.readlines()

for n in s:
    result = ''
    
    n = int(n)

    for i in [2]+list(range(3,n+1,2)):
        if n%i ==0:
            pn = None
            time = 0
            while n%i == 0:
                n = n//i
                pn = i
                time += 1
            if result != '':
                result += ' * '
            if time >1:
                result += f'{pn}^{time}'
            else:
                result += f'{pn}'

    print(result)