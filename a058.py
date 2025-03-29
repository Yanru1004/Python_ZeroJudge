n = int(input())

result =[0,0,0]
for i in range(n):
    m = int(input())
    result[m%3] += 1

print(' '.join([str(s) for s in result]))