t = int(input())
li = []
for i in range(1,int(1000**0.5)+1):
    li.append(i**2)

for i in range(t):
    a,b = int(input()),int(input())
    result = 0
    for x in range(a,b+1):
        if x in li:
            result += x

    print(f'Case {i+1}: {result}')
