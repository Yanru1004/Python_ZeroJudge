import sys

k = ord('*') - ord('1')

a = sys.stdin.readlines()

for s in a:
    result = ''
    for c in s:
        result += (chr(ord(c)+k))
    print(result)
