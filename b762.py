# b762. 英國聯蒙
#2025.06.29 AC

#戰績初始
score = {"kill":0,"die":0,"assist":0}
#連殺初始
combo = 0

#讀入命令數
com_num = int(input())

for i in range(com_num):
    command = input().strip()

    if command == "Die": #死亡訊息
        if combo < 3:
            print("You have been slained.")
        else:
            print('SHUTDOWN.')
        score['die'] += 1
        combo = 0

    elif command == 'Get_Kill': #擊殺訊息
        combo += 1
        if combo < 3:
            print('You have slain an enemie.')
        elif 3 <= combo <= 7:
            massage=[
                "KILLING SPREE!",
                "RAMPAGE~",
                "UNSTOPPABLE!",
                "DOMINATING!",
                "GUALIKE!"]
            print(f'{massage[combo - 3]}')
        else:
            print('LEGENDARY!')
        score['kill'] += 1
    else:
        score['assist'] += 1

#輸出戰績
print(f"{score['kill']}/{score['die']}/{score['assist']}")