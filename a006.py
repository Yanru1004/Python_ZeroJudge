import math

a,b,c = [int(n) for n in input().split()]

check = math.pow(b,2) - 4*a*c

if check < 0:
    print('No real root')

elif check == 0:
    
    print(f"Two same roots x={int(-b/(2*a))}")

else:
    x1 = int((-b + math.sqrt(check)) / 2*a)
    x2 = int((-b - math.sqrt(check)) / 2*a)
    print(f"Two different roots x1={x1} , x2={x2}")