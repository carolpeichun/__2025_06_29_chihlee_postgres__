import argparse
import random

def get_user_name()->str:
    """
    從命令列參數解析使用者姓名，若未提供則提示使用者輸入。

    使用 argparse 接收 '-n' 或 '--name' 參數作為姓名。如果未從命令列提供姓名，
    則會互動式地要求使用者輸入姓名。

    回傳值:
        str: 使用者從命令列或輸入取得的姓名。
    """
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name

def play_game(name:str)->None:
    """
    啟動一個猜數字遊戲，讓玩家在指定範圍內猜隨機產生的數字。

    參數:
        name (str): 玩家名稱，用於顯示猜測次數等訊息。

    遊戲流程:
        - 隨機產生一個介於 1 到 100 之間的整數作為目標數字。
        - 玩家每次輸入一個猜測數字，程式會提示數字範圍。
        - 若猜對，顯示成功訊息與猜測次數。
        - 若猜錯，根據猜測結果調整範圍並提示玩家繼續猜。
        - 若輸入不在範圍內，提示玩家重新輸入。
    """
    i = 0
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")

def main(): 
    frequency = 1
    name = get_user_name()
    for i in range(frequency):
        play_game(name)
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()