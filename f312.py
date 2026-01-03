#f312. 人力分配
#2025.12.14 AC

#讀取參數
a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())

#讀取員工數量
total_worker = int(input())

#設定初始效益
max_output = None

def calc_out(worker:int,a:int,b:int,c:int):
    output = a * (worker**2) + b * worker + c
    return output

for worker_A in range(total_worker+1):
    worker_B = total_worker - worker_A

    output = calc_out(worker_A,a1,b1,c1) + calc_out(worker_B,a2,b2,c2)

    if max_output == None or output > max_output:
        max_output = output

print(max_output)