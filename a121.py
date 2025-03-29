def isPrime(n):
    return n>=2 and any((n%i==0 for i in range(2,int(n**0.5+1))))

while True:
    try:
        n,m = input().strip().split()
        print(isPrime(n),isPrime(m))

    except:
        break