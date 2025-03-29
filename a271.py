n = int(input())

for i in range(n):
    r,w,y,b,p,h =[int(a) for a in input().strip().split(' ')]
    poison = 0
    try:
        eat = [int(a) for a in input().strip().split(' ')]
    except ValueError:
        print(f'{h}g')
        continue
    
    
    for e in eat:
        
        h -= poison * p
        
        if h <= 0:
            print('bye~Rabbit')
            break
        
        h += [0,r,w,-y,-b][e]
        
        if e ==4:
            poison += 1
            
        if h <=0:
            print('bye~Rabbit')
            break
    else:
        print(f'{h}g')
