#c290. APCS 2017-0304-1秘密差
#2025.12.12 AC

#讀取X值
X = input()

odd_sum  = sum([int(n) for n in X[0::2]])
even_sum = sum([int(n) for n in X[1::2]])

Y = abs(odd_sum - even_sum)

print(Y)
