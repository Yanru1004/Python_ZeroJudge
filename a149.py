n = int(input())

for i in range(n):
    s = input()
    result = 1
    for m in s:
        result *= int(m)
    print(result)