import sys
while True:
    try:
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        pw = input() #取得正確密碼
        if pw == '': #跳過空行
            continue 
        pw = pw.strip().split(' ')
        n = int(input()) #取得猜數字次數

        #猜數字迴圈開始
        for i in range(n):
            guess = input().strip().split(' ') #取得猜數字資訊

            index = [0,1,2,3]
            #a = 0
            b = 0
            #計算數字及位置皆正確數量
            print(pw,guess)
            for x in range(4):
                if pw[x] == guess[x]:
                    print
                    guess[x] = 'x'
                    index.pop(x)
            print(guess,index)
            for y in index:
                if pw[y] in guess:
                    b += 1
            
            print(f'{4-len(index)}A{b}B')
=======
=======
>>>>>>> Stashed changes
        pw = sys.stdin.readline()[:-1]
        if pw == '':
            continue
        pw = pw.strip().split(' ')
           
        #猜數字次數迴圈
        for i in range(int(sys.stdin.readline()[:-1])): #
                        
            b = 0
            guess = sys.stdin.readline()[:-1].split(' ')
                     
            for x in range(4):
                if pw[x] == guess[x]:
                    guess[x] ='x'                    
            
            for y in range(4):
                if guess[y] != 'x' and pw[y] in guess:
                
                    guess[guess.index(pw[y])] = 'o'
            

            print('{}A{}B'.format(guess.count('x'),guess.count('o')))
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        
    except:
        break